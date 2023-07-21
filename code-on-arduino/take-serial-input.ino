/*
On the serial port the input data will come in the format 10,2,3,4 basically 4 comma seperated values.

This code will seperate it into 4 values and then run a function on each value.

The first value is # of screw turns for Motor A X Axis
The second value is # of screw turns for Motor A Y Axis

The third value is # of screw turns for Motor B X Axis
The fourth value is # of screw turns for Motor B Y Axis

So there are 4 kinds of screw turns. 2 for Motor A (X and Y Axis) and 2 for Motor B (X and Y axis)
*/

// Motor control pins
int motorA_step_pin = 11; // B step pin
int motorA_dir_pin = 10; // B direction pin
int motorB_step_pin = 9; // C step pin
int motorB_dir_pin = 8; // C direction pin

void setup()
{
  // start serial port at 9600 bps and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  // set the motor control pins as outputs
  pinMode(motorA_step_pin, OUTPUT); 
  pinMode(motorA_dir_pin, OUTPUT); 
  pinMode(motorB_step_pin, OUTPUT); 
  pinMode(motorB_dir_pin, OUTPUT); 
}

void do_steps(int dir, int turns, int step_pin, int dir_pin) {
  digitalWrite(dir_pin, dir);
  for(int n = 0; n < turns; n++) {
    digitalWrite(step_pin, 1);
    delay(1);
    digitalWrite(step_pin, 0);
    delay(1);
  }
}

void loop()
{
  if (Serial.available() > 0) {
    String incomingString = Serial.readStringUntil('\n'); // read the incoming data as a string until newline
    incomingString.trim(); // remove any leading/trailing whitespace

    // Split the incoming string by commas into an array
    int incomingData[4];
    int index = 0;
    for (int i = 0; i < incomingString.length(); i++) {
      if (incomingString[i] == ',') {
        index++;
      } else {
        incomingData[index] = incomingData[index] * 10 + (incomingString[i] - '0');
      }
    }

    // Extract the number of turns for each Motor and axis
    int motorA_X_turns = incomingData[0];
    int motorA_Y_turns = incomingData[1];
    int motorB_X_turns = incomingData[2];
    int motorB_Y_turns = incomingData[3];

    // Execute steps based on the number of turns for each Motor and axis
    do_steps(1, motorA_X_turns, motorA_step_pin, motorA_dir_pin);
    do_steps(1, motorA_Y_turns, motorB_step_pin, motorB_dir_pin);
    do_steps(1, motorB_X_turns, motorA_step_pin, motorA_dir_pin);
    do_steps(1, motorB_Y_turns, motorB_step_pin, motorB_dir_pin);
  }
}
