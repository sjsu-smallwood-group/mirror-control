#define TOTAL_TRAVEL 264200
#define MIDPOINT TOTAL_TRAVEL / 2

// Control Channel B (horizontal)
long current_posB = MIDPOINT;

// Control Channel C (vertical)
long current_posC = MIDPOINT;

int cspeed = 200; // Constant speed for both channels

void setup()
{
  // start serial port at 9600 bps and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }
 
  // set the motor control pins as outputs
  pinMode(11, OUTPUT); // B step pin
  pinMode(10, OUTPUT); // B direction pin
  pinMode(9, OUTPUT); // C step pin
  pinMode(8, OUTPUT); // C direction pin
}

void do_steps(int dir, long &current_pos, int step_pin, int dir_pin) {
  digitalWrite(dir_pin,dir);
  for(int n = 0; n < cspeed; n++) {
    digitalWrite(step_pin,1);
    delay(1);
    digitalWrite(step_pin,0);
    delay(1);
    current_pos += step_dir;
  }
}

void loop()
{
  if (Serial.available() > 0) {
    int in = Serial.read(); // This will get value like  0,0,1,0
    do_steps(1, current_posB, 11, 10); 
  }
}
