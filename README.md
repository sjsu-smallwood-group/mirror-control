This system will create an experiment notebook that looks like this:

![Screenshot of end goal](./docs/experiments-notebook-on-7-24-2023.png)

The app controlling the mirrors look like this:

![Screenshot of app](./docs/screenshot-of-app.png)

The lab setup looks like this:

<img width="920" alt="Screenshot 2023-07-24 at 7 16 27 PM" src="https://github.com/sjsu-smallwood-group/mirror-control/assets/121723290/bbcef07f-68bb-4049-a933-76ff2e0a2819">

Picture of the connections between the computer to the Ardunio Uno R3, picomotor driver A and B, and mirror 1 and 2:

![IMG_4082](https://github.com/sjsu-smallwood-group/mirror-control/assets/121723290/c6e1829e-dca0-4064-a9f5-e585cf6e8f29)

The arduino controlling the mirrors looks like this:

![IMG_4091](https://github.com/sjsu-smallwood-group/mirror-control/assets/121723290/75815874-d275-42b6-85bf-a577f9438966)

Circuit diagram for controlling 2 picomotors using Arduino Uno R3 (Digital):

![Copy of Circuit diagram for synchonizing two picomotors (Digital)](https://github.com/sjsu-smallwood-group/mirror-control/assets/121723290/e2733789-7c69-4625-9b24-05ddc6ae694a)

# How to run this app on mac?

## Step 1

```
git clone https://github.com/sjsu-smallwood-group/mirror-control-js.git
cd mirror-control
> ./run-gui-serial-port-com.sh
```

The above script will start 2 subsystems:
Subsystem1: Run gui
Subsystem2: Run serial-port-communicator

## Step 2

After step 1 we need to start Subsystem3 i.e the app on arduino. To do that, you need to open the arduino IDE and open the file `code-on-arduino/take-serial-input.ino` and then click the upload button.

# System diagram

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
    sample TEXT,
    collaborator TEXT,
    experiementRanBy TEXT,
    temp_kelvin TEXT,
    notes TEXT,
    image BLOB
    motor1_abs_X INTEGER,
    motor1_abs_Y INTEGER,
    motor2_abs_X INTEGER,
    motor2_abs_Y INTEGER,
    dateTimeUpdated TEXT,
)
```

Video that explains how to start the program:
https://drive.google.com/file/d/145L-uPAMrEC0yE-OpZWiD-maVv1Q035u/view?usp=sharing

