from DIPPID import SensorUDP
import time,os

class Test:

  def __init__(self) -> None:
    self.sensor = SensorUDP(5700)
    self.counter = 0

  def test(self, _):
    self.counter += 1

  def run(self):
    self.time = time.time()
    self.duration = 10
    self.sensor.register_callback("rotation", self.test)
    self.sensor.register_callback("accelerometer", self.test)
    self.sensor.register_callback("gyroscope", self.test)

    while True:
      if self.time + self.duration < time.time():
        print(self.counter / self.duration)
        os._exit(0)

a = Test()
a.run()

#averaging around 77 callbacks per second;