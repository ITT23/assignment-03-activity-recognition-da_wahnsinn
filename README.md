# Assignment 3

Yu Liu, Michael Bierschneider

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/5mFcHVfA)

## Info

1. replaced dashes in python files for underscore (see https://peps.python.org/pep-0008/#package-and-module-names)
2. android dippid does not return angle values

## Setup

1. `source ./.venv/bin/activate`
2. `python -m pip install -r requirements.txt`

## Task 1

see `machine-learning-papers.md`

## Task 2

- start with `python gater-data.py [user_name] [activity] [-d [duration]] [-pps [polls_per_second]] [-w [wait]]`.
- `user_name` is required; should a string or integer to identify user.
- `activity` is required; can be `["standing", "lying", "jumping"]`.
- `-d` is optional; default 10 seconds; determines the duration in seconds that sensor values are recorded.
- `-pps` is optional; default 50 per second; determines the frequency the DIPPID device is polled per second; too many polls lead to duplicate values;
- `-w`is optional; default 5 seconds; time after pressing the button to start recording until the recording actually starts; gives the user the chance to put the device in his pocket and get ready for the activity to be recorded;
- `./archive/callback_count.py` shows that callbacks are called around 77 times per second with `["accelerometer", "gyroscope", "rotation"]`.
- after starting the application from the terminal, it waits until `button_1` is pressed. then the application sleeps for selected wait time (default 5 seconds) so that there is time to put it in your pockets and start with the activitiy so that there is no missleading data in the csv files.
- after the set duration, the application automatically terminates after creating a csv file from the collected data.

### Example

- start application with `python gather-data.py micha lying -d 5 -pps 100`.
- after pressing `button_1`, the application records sensor data at around 100 per second for 5 seconds.
- the application waits for 5 seconds after pressing the button before actually recording to give the user the chance to put the device in his pocket.
- after this time, the applications terminates creating a csv file with the name `./data/micha_LYING_1683818719103.csv`.

### how we sampled data

- with m5stack and android handy.
- android smartphones do not return angle values.
- while performing recording we put the DIPPID device in the right back pantspocket.
- a wait timer helped putting the DIPPID device in the pocket and start with the activity.
- we put it in the right back-pants-pocket so that the Y axis is parallel with the gravitational vector and shows in the same direction.
- we also sampled waving data but it showed that the prediction models can no differentiate so easily whichfore we droped theses csv files for the assignment.
- we also droped csv files with user_name yu and stefan because they had no rotation data.

## Task 3

- start gui application with `python activity_visualizer.py`.
- start terminal application with `pyhton activity_recogniser.py`.
- pressing ESC closes the gui application while the terminal application must be quit with ctrl+c
- recogniser class first loads all data from ./data and drops timestamp, user_name and measurement_id.
- recogniser trains a SVM model with this data.
- live data from M5Stack are assigned to a length-50 deque so that only live data is passed to the live prediction function.

## References

standing man -> https://unsplash.com/@james2k
waving man -> https://unsplash.com/@juniperphoton
jumping woman -> https://unsplash.com/@vultar
lying man -> https://unsplash.com/@rayner
unknown woman -> https://unsplash.com/@chris_ainsworth
