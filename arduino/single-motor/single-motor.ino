#include "BTS7960.h"

const uint8_t EN = 13;

const uint8_t EN_R = 12;
const uint8_t L_PWM = 9;
const uint8_t R_PWM = 10;
bool standby = false;

//BTS7960::BTS7960(uint8_t L_EN, uint8_t R_EN, uint8_t L_PWM, uint8_t R_PWM)
BTS7960 motorController(32,33,2, 3);

// BTS7960 MC1(32,33,2, 3);  L = forward 
// BTS7960 MC2(34,35,4, 5);  L = forward
// BTS7960 MC3(36,37,6, 7);  L = forward 
// BTS7960 MC4(38,39,8, 9);  

void setup() 
{
  Serial.begin(9600);
}

void loop() 
{  
  if (standby== true) {
    motorController.Enable();
    Serial.println("Motors enable" );
	   
    for(int t = 10 ; t > 0; t-=1)
    {
      Serial.println("standby t minus: "+String(t) );
      motorController.TurnLeft(0);
      delay(1000);
      motorController.TurnRight(0);
    }

  }else {

    
    
    delay(2000); 
    Serial.println("apagado ");
    
    delay(2000);
    
    Serial.println("voy a arrancar ");
    
    delay(3000);

    motorController.Enable();
    /*
    for(int speed = 30 ; speed < 60; speed+=20)
    {
      motorController.TurnLeft(speed);
      Serial.println("speed up L "+String(speed) );
      delay(1000);
      
      motorController.TurnRight(speed);
      
      Serial.println("speed up R "+String(speed) );
    }  
    */

    for(int speed = 80 ; speed < 100; speed+=5)
    {
      motorController.TurnLeft(speed);
      Serial.println("speed up L "+String(speed) );
      delay(2000);
      
      
      /* motorController.TurnRight(speed);
      Serial.println("speed up R "+String(speed) );
      delay(3000);
      */   
      
    }  

    for(int speed = 80 ; speed < 100; speed+=5)
    {
      motorController.TurnRight(speed);
      Serial.println("speed up R "+String(speed) );
      delay(2000);
      
      
      /* motorController.TurnRight(speed);
      Serial.println("speed up R "+String(speed) );
      delay(3000);
      */   
      
    }  
    motorController.Stop();
    /*
    for(int speed = 255 ; speed > 0; speed-=20)
    {
      motorController.TurnLeft(speed);
      Serial.println("speed down L "+String(speed) );
      delay(100);
    }  
    motorController.Stop();

  for(int speed = 0 ; speed < 255; speed+=40)
    {
      motorController.TurnRight(speed);
      Serial.println("speed up R "+String(speed) );
      delay(500);
    }  

    motorController.Stop();
    
    for(int speed = 255 ; speed > 0; speed-=40)
    {
      motorController.TurnRight(speed);
      Serial.println("speed down R: "+String(speed) );
      delay(500);
    }
  */

  }
  
  motorController.Stop();

  motorController.Disable();
  
 
}