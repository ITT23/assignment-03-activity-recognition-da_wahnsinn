# Assignment 3

Yu Liu, Michael Bierschneider

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/5mFcHVfA)

## Setup

1. `source ./.venv/bin/activate`
2. `python -m pip install -r requirements.txt`

## Task 1

WIP

## Task 2

- start with `python gater-data.py [user_name] [activity] [-d [duration]] [-pps [polls_per_second]] [-w [wait]]`
- `user_name` is required; should a string or integer to identify user
- `activity` is required; can be `["waving", "standing", "lying", "jumping"]`
- `-d` is optional; default 10 seconds; determines the duration in seconds that sensor values are recorded
- `-pps` is optional; default 50 per second; determines the frequency the DIPPID device is polled per second; too many polls lead to duplicate values;
- `-w`is optional; default 4 seconds; time after pressing the button to start recording until the recording actually starts; gives the user the chance to put the device in his pocket and get ready for the activity to be recorded;
- `./archive/callback_count.py` shows that callbacks are called around 77 times per second with `["accelerometer", "gyroscope", "rotation"]`.
- after starting the application from the terminal, it waits until `button_1` is pressed.
- after the set duration, the application automatically terminates after creating a csv file from the collected data.

### Example

- start application with `python gater-data.py micha lying -d 5 -pps 100`
- after pressing `button_1`, the application records sensor data at around 100 per second for 5 seconds.
- the application waits for 4 seconds after pressing the button before actually recording to give the user the chance to put the device in his pocket.
- after this time, the applications terminates creating a csv file with the name `./data/micha_LYING_1683818719103.csv`.

### how we sampled data

with m5stack and android handy
while performing recording we put the DIPPID device in the right back pantspocket
we put it in the pantspocket so that the Y axis is parallel with the gravitational vector

## Task 3

WIP
