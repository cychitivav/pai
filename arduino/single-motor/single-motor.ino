/*
  Control a single motor using BTS7960

  This code is for controlling a single motor using BTS7960. The motor is a 24V DC motor with 16A max current (JCF63R-2480-160). The BTS7960 is a 43A H-Bridge motor driver.

  Hardware Required:
  - Arduino Board with 2 PWM pins
  - BTS7960
  - 24V DC motor
  - 24V power supply

  Connections:
  - Connect 24V power supply to BTS7960
  - Connect 24V DC motor to M+ and M- of BTS7960
  - Connect GND of Arduino to GND of BTS7960
  - Connect enable signals of BTS7960 to digital pins of Arduino
  - Connect PWM signals of BTS7960 to PWM pins of Arduino

  Libraries Required (unzip and copy to documents/Arduino/libraries):
  - BTS7960:
    https://github.com/luisllamasbinaburo/Arduino-BTS7960/

    Note: Change delay in BTS7960.hpp to 1000 us

  Created by Sebastian Dueñas
  Last updated on Jun/18/2023
*/

// PINOUT
// L_EN -> 8
// R_EN -> 8
// L_PWM -> 9
// R_PWM -> 10

#include "BTS7960.h"

const uint8_t L_EN = 13;
const uint8_t R_EN = 12;

const uint8_t L_PWM = 9;
const uint8_t R_PWM = 10;

// BTS7960::BTS7960(uint8_t L_EN, uint8_t R_EN, uint8_t L_PWM, uint8_t R_PWM)
BTS7960 motorController(L_EN, R_EN, L_PWM, R_PWM);

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  motorController.Enable();
  Serial.println("Motor enable");

  motorController.TurnLeft(0);
  motorController.TurnRight(0);
  delay(2000);
  Serial.println("Turn off motor");

  Serial.println("Turn left (forward)");
  delay(3000);

  for (int speed = 80; speed < 100; speed += 5)
  {
    motorController.TurnLeft(speed);
    Serial.println("Speed up L " + String(speed));
    delay(2000);
  }

  Serial.println("Turn right (reverse)");
  delay(0);

  for (int speed = 80; speed < 100; speed += 5)
  {
    motorController.TurnRight(speed);
    Serial.println("Speed up R " + String(speed));
    delay(2000);
  }

  motorController.Disable();
  motorController.Stop();
  Serial.println("Motor disable");
}