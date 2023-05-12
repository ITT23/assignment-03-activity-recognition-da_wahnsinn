# this program gathers sensor data
import os, time, sys
from typing import TypedDict
from argparse import ArgumentParser, ArgumentTypeError
from enum import Enum

from DIPPID import SensorUDP


class Activity(Enum):
  WAVING = 1
  STANDING = 2
  LYING = 3
  JUMPING = 4


#own code: https://github.com/ITT23/assignment-01-dippid-and-pyglet-vairasza/blob/master/2d-game/main.py
class Input:

  T_Capa_State = TypedDict('CapaState', { 'accelerometer': dict, 'gyroscope': dict, 'rotation': dict })

  def __init__(self, port: int, capabilities: list[str], button_key: str) -> None:
    self._port = port
    self._sensor = SensorUDP(self._port)
    
    self._capabilities = capabilities
    self.capa_state = {}

    #handle button_1 events separately so that we do not have to split it from the rest of the sensor data later
    self._button_key = button_key
    self._button_pressed = False
  
  def get_button_state(self) -> bool:
    '''
      returns boolean value that indicates if button_1 from M5Stack was pressed. M5Stack should only return `True` once in the application cylce as the start is depending on the button press and the stop is depending on a time function (duration).
    '''
    pressed = self._sensor.get_value(self._button_key)

    if pressed and pressed[1] and not self._button_pressed:
      self._button_pressed = True

      return True

    return False
  
  def get_capa_state(self) -> T_Capa_State:
    for capability in self._capabilities:
      data = self._sensor.get_value(capability)

      if data is not None:
        self.capa_state[data[0]] = data[1]

    return self.capa_state

  def terminate_sensor(self) -> None:
    self._sensor.disconnect()


class Application:

  PORT = 5700
  CURR_DIR = os.path.dirname(__file__)
  OUTPUT_FOLDER = "/data/"
  CAPABILITIES = ["accelerometer", "gyroscope", "rotation"]
  BUTTON_KEY = "button_1"
  CSV_HEADER = "measurement_id,user_name,time_stamp,activity,accelerometer_x,accelerometer_y,accelerometer_z,gyroscope_x,gyroscope_y,gyroscope_z,rotation_pitch,rotation_roll,rotation_yaw\n"

  def __init__(self, user_name: str, activity: Activity, duration: int, pps: int, wait: int) -> None:
    self._input = Input(self.PORT, self.CAPABILITIES, self.BUTTON_KEY)

    self._user_name = user_name
    self._activity = activity
    self._duration =  duration
    self._pps = 1 / pps #polls per second; callback mode averages around 77 per second (see archive/callback_count.py); setting default to 50 to avoid too many double measurements;
    self._wait = wait

    self._running = True
    self._recording = False
    
    self._measurement_id = 0
    self._data = []

  def run(self) -> None:
    start_time = None
    print("waiting for button_1 press to start recording...\n")

    while self._running:

      if self._input.get_button_state():
        print(f"* * * recording starts in {self._wait} seconds. * * *\n")
        time.sleep(self._wait)
        self._recording = True
        start_time = time.time()
        print(f"* * * recording has started at unix time {time.ctime(start_time)}. * * *\n")

      if self._recording:
        data = self._input.get_capa_state()
        self._process_sensor_data(data)

        if start_time + self._duration < time.time():
          self._recording = False
          print(f"* * * recording has stopped at unix time {time.ctime(time.time())}. * * *\n")
          self._input.terminate_sensor()
          self._write_csv_data()
          sys.exit()

      '''
        m5stack polling needs to be limited as sensor values do not change as often as python can call get_capa_state. this would leed to a lot of dublicate data.
      '''
      time.sleep(self._pps)

  def _process_sensor_data(self, data: dict) -> None:
    meta_data = f"{self._measurement_id},{self._user_name},{round(time.time() * 1000)},{self._activity.name}"
    
    measurement_data = ""
    for sensor_name in data:
      for axis_name in data[sensor_name]:
        measurement_data += f",{data[sensor_name][axis_name]}"

    self._data.append(meta_data + measurement_data)
    self._measurement_id += 1

  def _write_csv_data(self) -> None:
    content = self.CSV_HEADER
    content += "\n".join(self._data)

    file_path = f"{self.CURR_DIR}{self.OUTPUT_FOLDER}"
    file_name = f"{file_path}{self._user_name}_{self._activity.name}_{round(time.time() * 1000)}.csv"
    data_file = open(file_name, "w")
    data_file.write(content)
    data_file.close()
    print(f"file saved to {file_name}.")

def check_positive_int(value) -> bool:
  try:
    int_val = int(value)
    if int_val < 0:
      raise ArgumentTypeError(f"{value} is not a positive integer.")
    return int_val
  except Exception:
    raise ArgumentTypeError(f"{value} is not a positive integer.")


if __name__ == "__main__":
  parser = ArgumentParser(prog="Data Gatherer", description="this application gatheres activity data from a M5Stack or an Android smartphone. data contains these values: acceleration, gyroscope, angle and timestamp. data will be saved to a csv file.")
  parser.add_argument("user_name", type=str, help="provide a name that maps the activity pattern to a certain user.")
  parser.add_argument("activity", type=str, choices=["waving", "standing", "lying", "jumping"], help="provide an activity that you want to measure. activities are: waving, standing, lying and jumping.")
  parser.add_argument("-d", "--duration", default=10, type=check_positive_int, help="provide a duration in seconds that you want to measure your activity. the application automatically stops the recording and creates a csv file. (unit is SECONDS, must be greater than 0)")
  parser.add_argument("-pps", "--pollspersecond", default=50, type=check_positive_int, help="determine the frequency that the DIPPID device is polled for sensor data. (unit is SECONDS, must be greater than 0)")
  parser.add_argument("-w", "--wait", default=4, type=check_positive_int, help="when pressing button_1 to start recording, the application waits X second so that the user can put the device inside his pocket and get ready for the activity. (unit is SECONDS, must be greater than 0)")

  args = parser.parse_args()

  application = Application(args.user_name, Activity[args.activity.upper()], args.duration, args.pollspersecond, args.wait)
  application.run()