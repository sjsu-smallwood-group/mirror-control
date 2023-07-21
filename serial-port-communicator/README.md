Q1) What is the reason for existence of this program?
This takes the data from the GUI and sends it to the arduino.
This makes our system made up of smaller components that talk to each other instead of 1 large program.

Q2) How to run this program?

Install the dependencies:

> pip3 install pyserial watchdog

Run the program:

> python3 talk-to-arduino.py

Q3) How does this get data from gui?
It uses the experimental-results.sqlite as a data pipe. So when the GUI writes data to experimental-results.sqlite, this program reads it and sends it to the arduino.
