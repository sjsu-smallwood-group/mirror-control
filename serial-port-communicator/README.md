Q) How to run this program?
pip3 install pyserial watchdog
python3 talk-to-arduino.py

Q) How does this get data from gui?
It uses the experimental-results.sqlite as a data pipe. So when the GUI writes data to experimental-results.sqlite, this program reads it and sends it to the arduino.
