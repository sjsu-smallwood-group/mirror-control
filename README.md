This system will create an experimental log that looks like this:

![Screenshot of end goal](./docs/experimental-log-on-7-22-2023.png)

Updated on 7/24:

<img width="1669" alt="experiment-log-on7-24" src="https://github.com/sjsu-smallwood-group/mirror-control/assets/121723290/b5dbb40e-aa54-4c36-bbf5-e9121390c89c">


The app controlling the mirrors look like this:

![Screenshot of app](./docs/screenshot-of-app.png)

Updated on 7/24:

<img width="1270" alt="Screenshot-of-app 2023-07-24 at 11 54 48 AM" src="https://github.com/sjsu-smallwood-group/mirror-control/assets/121723290/3e635855-56ec-469a-b5f8-c3a65a41344b">


The lab setup looks like this:
![Picture of the lab setup](./docs/lab-setup.jpeg)

The arduino controlling the mirrors looks like this:
![Picture of the arduino controlling the mirrors](./docs/arduino-controlling-the-mirrors.jpeg)

Updated on 7/24:

![IMG_4087](https://github.com/sjsu-smallwood-group/mirror-control/assets/121723290/74f170fc-d1da-479e-ba80-b32cc059c253)


# How to run this app on mac?

git clone https://github.com/sjsu-smallwood-group/mirror-control-js.git
cd mirror-control

Subsystem1: Run gui
Subsystem2: Run serial-port-communicator
Subsystem3: Run code-on-arduino

> ./run-gui-serial-port-com.sh

## System diagram

```
+-----------+   USB   +------------+   Wires  +--------------+         +--------------+
| Computer  | <-----> | Arduino UNO| <------> |Mirror DriverA| <------>|    Mirror 1  |
|           |         |            |          | Picomotor    |         |              |
| running   |         | running    |          | Model: 8801  |         |              |
|           |         |            |          +--------------+         +--------------+
| electron  |         | take-      |
| gui       |         | serial-    |   Wires  +--------------+         +--------------+
|           |         | input.ino  | <------> |Mirror DriverB| <------>|    Mirror 2  |
+-----------+         +------------+          | Picomotor    |         |              |
                                              | Model: 8801  |         |              |
                                              +--------------+         +--------------+
```

# How to view the experimental logs?

1. Install https://sqlitebrowser.org/dl/

2. Then open the file experiments-notebook.sqlite inside the db browser app.

3. Catch up knowledge is at: https://www.youtube.com/watch?v=b0Dplx4M5zg

# What are the column names in the experimental log book?

```
CREATE TABLE tblObservations(
    id INTEGER PRIMARY KEY,
    material TEXT,
    experiementRanBy TEXT,
	temperature_kelvin TEXT,
	dateTimeUpdated TEXT,
    motor1_abs_X INTEGER,
	motor1_abs_Y INTEGER,
    motor2_abs_X INTEGER,
    motor2_abs_Y INTEGER,
    notes TEXT,
	image BLOB
  )
```
