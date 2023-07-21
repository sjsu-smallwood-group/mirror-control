import sqlite3
import time
import serial

# Serial port settings
port = "/dev/ttyACM0"  # replace with your Arduino's port
baud_rate = 9600

# SQLite settings
db_path = "../experimental-results.sqlite"
table_name = "sliders"

# connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# initialize the last seen ID and motor values
cursor.execute(
    "SELECT MAX(id), motorA_abs_X, motorA_abs_Y, motorB_abs_X, motorB_abs_Y FROM sliders"
)
(
    last_id,
    last_motorA_abs_X,
    last_motorA_abs_Y,
    last_motorB_abs_X,
    last_motorB_abs_Y,
) = cursor.fetchone()

print(
    "Starting to watch the data pipeline (experimental-results.sqlite) for new row inserts..."
)
while True:
    # get the last row's ID
    cursor.execute("SELECT MAX(id) FROM sliders")
    current_id = cursor.fetchone()[0]

    # check if there's a new row
    if current_id != last_id:
        last_id = current_id

        # fetch the new row's data
        cursor.execute("SELECT * FROM sliders WHERE id=?", (last_id,))
        row_data = cursor.fetchone()

        # fetch the column names
        column_names = [description[0] for description in cursor.description]

        # create a dictionary mapping column names to data
        row_dict = dict(zip(column_names, row_data))

        # calculate deltas
        motorA_delta_X = row_dict["motorA_abs_X"] - last_motorA_abs_X
        motorA_delta_Y = row_dict["motorA_abs_Y"] - last_motorA_abs_Y
        motorB_delta_X = row_dict["motorB_abs_X"] - last_motorB_abs_X
        motorB_delta_Y = row_dict["motorB_abs_Y"] - last_motorB_abs_Y

        # update last motor values
        last_motorA_abs_X = row_dict["motorA_abs_X"]
        last_motorA_abs_Y = row_dict["motorA_abs_Y"]
        last_motorB_abs_X = row_dict["motorB_abs_X"]
        last_motorB_abs_Y = row_dict["motorB_abs_Y"]

        # Send the data to the Arduino
        message = (
            f"{motorA_delta_X},{motorA_delta_Y},{motorB_delta_X},{motorB_delta_Y}\n"
        )

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
