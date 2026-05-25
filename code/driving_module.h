#ifndef DRIVING_MODULE_H
#define DRIVING_MODULE_H

//Controls driving features of Ca-R-oomba
class Car{
  public:
    int Right1 = 0;
    int Right2 = 0;

    int Left1 = 0;
    int Left2 = 0;

    int controlPin1 = 0;
    int controlPin2 = 0;

    Car(int pin1, int pin2, int pin3, int pin4, int pin5, int pin6){
      Right1 = pin1;
      Right2 = pin2;

      Left1 = pin3;
      Left2 = pin4; 

      controlPin1 = pin5;
      controlPin2 = pin6;
      
      //Right-Side Motors
      pinMode(Right1, OUTPUT);
      pinMode(Right2, OUTPUT);

      //Left-Side Motors
      pinMode(Left1, OUTPUT);
      pinMode(Left2, OUTPUT);
  
      //Control Pins
      analogWrite(controlPin1, 120);
      analogWrite(controlPin2, 120);
    }

    void forward(){
      analogWrite(controlPin1, 150);
      analogWrite(controlPin2, 150);

      digitalWrite(Right1, LOW);
      digitalWrite(Right2, HIGH);

      digitalWrite(Left1, LOW);
      digitalWrite(Left2, HIGH);
    }

    void backward(){
      analogWrite(controlPin1, 150);
      analogWrite(controlPin2, 150);
      
      digitalWrite(Right1, HIGH);
      digitalWrite(Right2, LOW);

      digitalWrite(Left1, HIGH);
      digitalWrite(Left2, LOW);
    }

    void right(){
      analogWrite(controlPin1, 255);
      analogWrite(controlPin2, 255);

      digitalWrite(Right1, HIGH);
      digitalWrite(Right2, LOW);

      digitalWrite(Left1, LOW);
      digitalWrite(Left2, HIGH);
    }

    void left(){
      analogWrite(controlPin1, 255);
      analogWrite(controlPin2, 255);

      digitalWrite(Right1, LOW);
      digitalWrite(Right2, HIGH);

      digitalWrite(Left1, HIGH);
      digitalWrite(Left2, LOW);
    }

    void stop(){
      digitalWrite(Right1, LOW);
      digitalWrite(Right2, LOW);

      digitalWrite(Left1, LOW);
      digitalWrite(Left2, LOW);
    }

    void command(String message){
      if (message == "forward"){forward();}
      else if(message == "backward"){backward();}
      else if(message == "left"){left();}
      else if(message == "right"){right();}
      else if(message == "stop"){stop();}
      else{stop();}
    }
};


#endif