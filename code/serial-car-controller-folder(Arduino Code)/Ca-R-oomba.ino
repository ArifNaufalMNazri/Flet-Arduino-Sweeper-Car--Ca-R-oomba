#include "driving_module.h"
#include "sweeper_module.h"

Servo servo_1;
Servo servo_2;

int servoPin1 = 6;
int servoPin2 = 7;

int trigPin1 = 12;
int echoPin1 = 13;

Car car(2, 3, 4, 5, 8, 11);

void setup() {
  Serial.begin(9600);

  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);

  servo_1.attach(servoPin1);
  servo_2.attach(servoPin2);
  
  servo_1.write(0);
  servo_2.write(0);
}

bool was_blocked = false;

void loop() {
  bool is_blocked = check_distance_cm(trigPin1, echoPin1);
  sweep(servo_1, servo_2,is_blocked);

  if(!is_blocked){
    if(Serial.available() > 0){
      String incomingData = Serial.readStringUntil('\n');
      car.command(incomingData);
    }
  }
  else if(is_blocked && was_blocked){
    car.command("stop");
    while(Serial.available() > 0){
      Serial.read();
    }
  }

  was_blocked = is_blocked;
}
