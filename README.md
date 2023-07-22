This system will create experimental log that look like this:

![Screenshot of end goal](./docs/experimental-log-on-7-22-2023.png)

The app controlling the mirrors look like this:

![Screenshot of app](./docs/screenshot-of-app.png)

The lab setup looks like this:
![Picture of the lab setup](./docs/lab-setup.jpeg)

The arduino controlling the mirrors looks like this:
![Picture of the arduino controlling the mirrors](./docs/arduino-controlling-the-mirrors.jpeg)

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
| Computer  | <-----> | Arduino UNO| <------> | Mirror Driver| <------>|    Mirror    |
|           |         |            |          | Picomotor    |         |              |
| running   |         | running    |          | Model: 8801  |         |              |
|           |         |            |          +--------------+         +--------------+
| electron  |         | take-      |
| gui       |         | serial-    |   Wires  +--------------+         +--------------+
|           |         | input.ino  | <------> | Mirror Driver| <------>|    Mirror    |
+-----------+         +------------+          | Picomotor    |         |              |
                                              | Model: 8801  |         |              |
                                              +--------------+         +--------------+
```
