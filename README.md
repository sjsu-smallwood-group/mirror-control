![Screenshot of app](./screenshot-of-app.png)

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
