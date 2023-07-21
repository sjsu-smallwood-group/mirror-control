import sqlite3
import time

# connect to the database
conn = sqlite3.connect("../experimental-results.sqlite")
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

while True:
    # get the last row's ID
    cursor.execute("SELECT MAX(id) FROM sliders")
    current_id = cursor.fetchone()[0]

    # check if there's a new row
    if current_id != last_id:
        # print("New row inserted!")
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

        # print(f"Row data: {row_dict}")
        print(f"motorA_delta_X: {motorA_delta_X}")
        print(f"motorA_delta_Y: {motorA_delta_Y}")
        print(f"motorB_delta_X: {motorB_delta_X}")
        print(f"motorB_delta_Y: {motorB_delta_Y}")

    # wait before checking again
    time.sleep(1)
