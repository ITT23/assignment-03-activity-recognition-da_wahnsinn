# this program recognises activities
import os, time
from typing import TypedDict
from collections import deque

import pandas as pd
import numpy as np
from numpy.typing import ArrayLike
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.metrics import accuracy_score

from DIPPID import SensorUDP
from activity import Activity

#own code: https://github.com/ITT23/assignment-01-dippid-and-pyglet-vairasza/blob/master/2d-game/main.py
class Input:

  T_Capa_State = TypedDict('CapaState', { 'accelerometer': dict, 'gyroscope': dict, 'rotation': dict })

  def __init__(self, port: int, capabilities: list[str]) -> None:
    self._port = port
    self._sensor = SensorUDP(self._port)
    
    self._capabilities = capabilities
    self.capa_state = {}
  
  def get_capa_state(self) -> T_Capa_State:
    for capability in self._capabilities:
      data = self._sensor.get_value(capability)

      if data is not None:
        self.capa_state[data[0]] = data[1]

    return self.capa_state

  def terminate_sensor(self) -> None:
    self._sensor.disconnect()


class TrainData:

  DROP_COLS = ["measurement_id", "user_name", "time_stamp"]

  def __init__(self, _work_dir: str) -> None:
    self._work_dir = _work_dir
    self._data = pd.DataFrame()
    self._read_dir()
    self._drop_cols()

  def _read_dir(self) -> None:
    csv_data = os.listdir(self._work_dir)

    for csv_file in csv_data:
      #unfortunately macos always creates these beautiful piles of bytes called .DS_Store therefore ignoring all files that are not a csv file.
      if not csv_file.endswith(".csv"):
        continue

      data = pd.read_csv(f"{self._work_dir}/{csv_file}")
      self._data = pd.concat([self._data, data])

  def _drop_cols(self) -> None:
    self._data = self._data.drop(self.DROP_COLS, axis=1)
    self._data.dropna(inplace=True)

  def get_data(self) -> pd.DataFrame:
    return self._data


class PredictionModel:

  TEST_SPLIT = 0.2
  RANDOM_STATE = 42
  KERNEL = "poly" #poly is slightly better than rbf; linear is really bad
  CLASS_LABEL = "activity"

  def __init__(self, data: pd.DataFrame) -> None:
    self._data = data
    
    self._normalised_data, self._scaler = self._scale_train_data(self._data)
    self._encoded_class, self._encoder = self._encode_activity(self._data)
    self._X_train, self._X_test, self._y_train, self._y_test = self._split_data()

  def _scale_train_data(self, train_data: pd.DataFrame) -> tuple[pd.DataFrame, MinMaxScaler]:
    train_data_values = train_data.values[:, 1:] #creates an np.ndarray without activity column

    scaler = MinMaxScaler()
    scaler.fit(train_data_values)
    scaled_samples = scaler.transform(train_data_values)

    normalised_samples = train_data_values.copy()
    normalised_samples = scaled_samples

    return normalised_samples, scaler

  def _encode_activity(self, data: pd.DataFrame) -> tuple[ArrayLike, LabelEncoder]:
    encoder = LabelEncoder()
    encoder.fit(data[self.CLASS_LABEL])

    return encoder.transform(data[self.CLASS_LABEL]), encoder

  def _split_data(self) -> list:
    X = self._normalised_data
    Y = self._encoded_class

    return train_test_split(X, Y, test_size=self.TEST_SPLIT, random_state=self.RANDOM_STATE)

  def train(self) -> None:
    self._svm = SVC(kernel=self.KERNEL)
    self._svm.fit(self._X_train, self._y_train)    

  def predict_test(self) -> np.ndarray:
    return self._svm.predict(self._X_test)

  def get_accuracy_score(self, prediction: list) -> float:
    return accuracy_score(self._y_test, prediction)

  def _transform_deque(self, data: list) -> pd.DataFrame:
    transformed_list = []

    for item in data:
      sub_list = []
      sub_list.append(item["accelerometer"]["x"])
      sub_list.append(item["accelerometer"]["y"])
      sub_list.append(item["accelerometer"]["z"])
      sub_list.append(item["gyroscope"]["x"])
      sub_list.append(item["gyroscope"]["y"])
      sub_list.append(item["gyroscope"]["z"])
      sub_list.append(item["rotation"]["pitch"])
      sub_list.append(item["rotation"]["roll"])
      sub_list.append(item["rotation"]["yaw"])
      transformed_list.append(sub_list)

    return pd.DataFrame(data=transformed_list, columns= ["accelerometer_x","accelerometer_y","accelerometer_z","gyroscope_x","gyroscope_y","gyroscope_z","rotation_pitch","rotation_roll","rotation_yaw"])

  def _scale_live_data(self, data: list) -> np.ndarray:
    df = np.array(self._transform_deque(data)) #to prevent UserWarning: X has feature names, but MinMaxScaler was fitted without feature names

    scaled_samples = self._scaler.transform(df)
    normalised_samples = df.copy()
    normalised_samples = scaled_samples

    return normalised_samples

  def predict_live(self, data: list) -> None:
    scaled_data = self._scale_live_data(data)
    
    prediction = self._svm.predict(scaled_data)
    activities = self._encoder.classes_[prediction]

    #prediction returns a list of activities found for the list auf m5stack values. using mode to find the most prominent activity.
    activities, counts = np.unique(activities, return_counts=True)
    index = counts.argmax()

    return activities[index]

class Recogniser:

  PORT = 5700
  CURR_DIR = os.path.dirname(__file__)
  DATA_PATH = "/data/"
  CAPABILITIES = ["accelerometer", "gyroscope", "rotation"]
  LABEL = "activity"
  DQ_MAX_LEN = 50
  PREDICTION_INTERVAL = 250
  PPS = 1 / 60

  def __init__(self) -> None:
    print("* * * reading training data * * *")
    self._input = Input(self.PORT, self.CAPABILITIES)
    self._train_data = TrainData(self.CURR_DIR + self.DATA_PATH)
    data = self._train_data.get_data()
    print("* * * DONE reading training data * * *")

    print("* * * training prediction model * * *")
    self._predict_model = PredictionModel(data)
    self._predict_model.train()
    prediction = self._predict_model.predict_test()
    print("* * * DONE training prediction model * * *")
    print("* * * model has an accuracy of {:.2f}. * * *".format(self._predict_model.get_accuracy_score(prediction)))

    print("* * * Starting activity predictions * * *")

    #we only want the last x elements from the m5stack for prediction because too old elements distort predicition and prediction would take too long
    self._deque_list = deque([], maxlen=self.DQ_MAX_LEN)
    self._current_activity = Activity.UNKNOWN
    self._start_time = time.time() * 1000 #using milliseconds

  def get_activity_gui(self) -> Activity:
    data = self._input.get_capa_state()

    if data:
      self._deque_list.append(data.copy()) #appending data without copying overwrote all entries :(
      now = time.time() * 1000

      # only predict an activity if deque is full; also use an interval of x seconds so that the data in deque has refreshed an the activity does no jump every x ms
      if (len(self._deque_list) == self.DQ_MAX_LEN) and (now - self._start_time >= self.PREDICTION_INTERVAL):
        detected_activity = self._predict_model.predict_live(self._deque_list.copy())
        self._current_activity = Activity[detected_activity]

        self._start_time = time.time() * 1000

    return self._current_activity

  def get_activity_terminal(self) -> Activity:
    while True:
      data = self._input.get_capa_state()

      if data:
        self._deque_list.append(data.copy()) #appending data without copying overwrote all entries :(
        now = time.time() * 1000

        # only predict an activity if deque is full; also use an interval of x seconds so that the data in deque has refreshed an the activity does no jump every x ms
        if (len(self._deque_list) == self.DQ_MAX_LEN) and (now - self._start_time >= self.PREDICTION_INTERVAL):
          detected_activity = self._predict_model.predict_live(self._deque_list.copy())
          self._current_activity = Activity[detected_activity]

          self._start_time = time.time() * 1000

      print(f"current activity is {self._current_activity.name}")
      time.sleep(self.PPS)

if __name__ == "__main__":
  recogniser = Recogniser()
  recogniser.get_activity_terminal()