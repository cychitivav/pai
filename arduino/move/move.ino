#include "BTS7960.h"

const uint8_t EN = 13;

const uint8_t EN_R = 12;
const uint8_t L_PWM = 9;
const uint8_t R_PWM = 10;
bool standby = false;
long right_motors_speed;
long lef_motors_speed;

long lineal_speed = 0;
long angular_speed = 0;

//  L = forward
// MC1: RF
// MC2: RB
// MC3: LF
// MC4: LB

BTS7960 MC1(32, 33, 2, 3);
BTS7960 MC2(34, 35, 4, 5);
BTS7960 MC3(36, 37, 6, 7);
BTS7960 MC4(38, 39, 8, 9);

void setup()
{
  Serial.begin(9600);
}

void loop()
{

  delay(2000);
  Serial.println("apagado ");

  delay(2000);

  Serial.println("voy a arrancar ");

  delay(3000);
  angular_speed = 0;
  vehicle_enable();

  /*
    for(int lineal_speed = 40 ; lineal_speed <260; lineal_speed+=40)
    {
      vehicle_move(lineal_speed, angular_speed);
      delay(2000);


    }
    for(int lineal_speed = 240 ; lineal_speed >40; lineal_speed-=40)
    {
      vehicle_move(lineal_speed, angular_speed);
      delay(2000);


    }
    vehicle_stop();
    vehicle_enable();
    for(int lineal_speed = -40 ; lineal_speed >-260; lineal_speed-=40)
    {
      vehicle_move(lineal_speed, angular_speed);
      delay(2000);
    }

    for(int lineal_speed = -260 ; lineal_speed <-40; lineal_speed+=40)
    {
      vehicle_move(lineal_speed, angular_speed);
      delay(2000);


    }
    lineal_speed = 0;
    vehicle_stop();
    vehicle_enable();


  */
  lineal_speed = 0;
  for (int angular_speed = 200; angular_speed < 260; angular_speed += 2)
  {
    vehicle_move(lineal_speed, angular_speed);
    delay(2000);
  }

  vehicle_stop();
}
void vehicle_enable()
{
  MC1.Enable();
  MC2.Enable();
  MC3.Enable();
  MC4.Enable();
}
void vehicle_stop()
{

  MC1.Stop();
  MC2.Stop();
  MC3.Stop();
  MC4.Stop();

  MC1.Disable();
  MC2.Disable();
  MC3.Disable();
  MC4.Disable();
  delay(2000);
}
void vehicle_move(int lineal_speed, int angular_speed)
{

  int right_motors_speed = lineal_speed + angular_speed;
  int left_motors_speed = lineal_speed - angular_speed;
  MC1.Move(right_motors_speed);
  MC2.Move(right_motors_speed);
  MC3.Move(left_motors_speed);
  MC4.Move(left_motors_speed);
  Serial.println("speed L " + String(left_motors_speed) + " speed R " + String(right_motors_speed));
}
