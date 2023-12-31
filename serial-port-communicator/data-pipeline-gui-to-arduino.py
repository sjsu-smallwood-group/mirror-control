import sqlite3
import time
import serial
import json
import os

# Load configuration file
config_file_path = os.path.join(os.path.dirname(__file__), "config.json")
with open(config_file_path, "r") as f:
    config = json.load(f)

# Serial port settings
port = config["port"]  # get port from configuration
baud_rate = 9600

# SQLite settings
db_path = "../experiments-notebook.sqlite"
table_name = "observations"

# connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# initialize the last seen ID and motor values
cursor.execute(
    "SELECT MAX(id), motor1_abs_X, motor1_abs_Y, motor2_abs_X, motor2_abs_Y FROM tblObservations"
)
(
    last_id,
    last_motor1_abs_X,
    last_motor1_abs_Y,
    last_motor2_abs_X,
    last_motor2_abs_Y,
) = cursor.fetchone()

print(port)
print("Watching data pipeline (experiments-notebook.sqlite) for new row inserts...")
while True:
    # get the last row's ID
    cursor.execute("SELECT MAX(id) FROM tblObservations")
    current_id = cursor.fetchone()[0]

    # check if there's a new row
    if current_id != last_id:
        last_id = current_id

        # fetch the new row's data
        cursor.execute("SELECT * FROM tblObservations WHERE id=?", (last_id,))
        row_data = cursor.fetchone()

        # fetch the column names
        column_names = [description[0] for description in cursor.description]

        # create a dictionary mapping column names to data
        row_dict = dict(zip(column_names, row_data))

        # calculate deltas
        motor1_delta_X = row_dict["motor1_abs_X"] - last_motor1_abs_X
        motor1_delta_Y = row_dict["motor1_abs_Y"] - last_motor1_abs_Y
        motor2_delta_X = row_dict["motor2_abs_X"] - last_motor2_abs_X
        motor2_delta_Y = row_dict["motor2_abs_Y"] - last_motor2_abs_Y

        # update last motor values
        last_motor1_abs_X = row_dict["motor1_abs_X"]
        last_motor1_abs_Y = row_dict["motor1_abs_Y"]
        last_motor2_abs_X = row_dict["motor2_abs_X"]
        last_motor2_abs_Y = row_dict["motor2_abs_Y"]

        # Send the data to the Arduino
        message = (
            f"{motor1_delta_X},{motor1_delta_Y},{motor2_delta_X},{motor2_delta_Y}\n"
        )

        print(message)

        try:
            ser = serial.Serial(port, baud_rate)
            time.sleep(2)  # give the connection a second to settle
            ser.write(message.encode())
            ser.close()
        except serial.SerialException as e:
            with open("debug.txt", "a") as f:  # open the file in append mode
                f.write(f"Failed to send message: {message} Error: {e}\n")

    # wait before checking again
    time.sleep(1)
