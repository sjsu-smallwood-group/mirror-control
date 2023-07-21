import time
import sqlite3
import serial
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

# Serial port settings
port = "/dev/ttyACM0"  # replace with your Arduino's port
baud_rate = 9600

# SQLite settings
db_path = "../experimental-results.sqlite"
table_name = "sliders"

# Watchdog settings
watch_patterns = [db_path]
watch_ignore_patterns = []
watch_ignore_directories = False
watch_case_sensitive = True

# Global variable to hold the last ID processed
last_id_processed = 0


def on_modified(event):
    print("File modified: ", event.src_path)
    global last_id_processed

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get the last row
    query = f"SELECT * FROM {table_name} ORDER BY id DESC LIMIT 1"
    cursor.execute(query)
    row = cursor.fetchone()

    # Check if there's a new row
    if row and row[0] != last_id_processed:
        last_id_processed = row[0]

        # Get the relevant fields
        motor_a_x = row[2]
        motor_a_y = row[3]
        motor_b_x = row[4]
        motor_b_y = row[5]

        # Create the serial connection
        ser = serial.Serial(port, baud_rate)
        time.sleep(2)  # give the connection a second to settle

        # Send the data to the Arduino
        message = f"{motor_a_x},{motor_a_y},{motor_b_x},{motor_b_y}\n"
        print("Sending message to Arduino: ", message)  # add this line
        ser.write(message.encode())

        # Close the serial connection
        ser.close()

    # Close the database connection
    conn.close()


if __name__ == "__main__":
    event_handler = PatternMatchingEventHandler(
        watch_patterns,
        watch_ignore_patterns,
        watch_ignore_directories,
        watch_case_sensitive,
    )
    event_handler.on_modified = on_modified

    observer = Observer()
    observer.schedule(event_handler, ".", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
