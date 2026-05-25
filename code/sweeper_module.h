#ifndef SWEEPER_MODULE_H
#define SWEEPER_MODULE_H
#include <Servo.h>

//Controls sweeping feature of Ca-R-oomba
bool check_distance_cm(int trigPin, int echoPin){
  
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  long time = pulseIn(echoPin, HIGH, 20000);

  if(time == 0){
    return false;
  }

  long distance_cm = time / 29 / 2;

  if(distance_cm < 6 && distance_cm > 0){
    return true;
  }
  else{
    return false;
  }
}

void sweep(Servo &servo_1, Servo &servo_2, bool sweeper_state){

  if(sweeper_state){
      servo_1.write(70);
      servo_2.write(70);
      delay(500);
   
      servo_1.write(0);
      servo_2.write(0);
      delay(500);
  }
 
}
#endif