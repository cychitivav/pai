/*
  Battery voltage measurement using ATtiny85 ADC

  This code is for measuring battery voltage using ATtiny85 ADC and sending 
  the value to master device via i2c. The address of the slave device is 
  0x08 and can be changed in the code.

  Hardware Required:
    - ATtiny85

  Connections:
    - Connect battery voltage to PB2 (ADC1)
    - Connect SDA to PB0
    - Connect SCL to PB2
    - Connect GND to GND
    - Connect VCC to VCC

    Note: ATtiny85 only can read voltages up to VCC, so if you want to 
    measure voltages higher than 5V, you need to use a voltage divider.

  Libraries Required (unzip and copy to documents/Arduino/libraries):
    - TinyWireS:
        https://playground.arduino.cc/uploads/Code/TinyWireS/index.zip

  Programming:
    - Connect ATtiny85 to Arduino Uno
    - Upload ArduinoISP sketch to Arduino Uno
    - Select "Arduino as ISP" programmer
    - Burn bootloader
    - Select "Arduino as ISP" programmer
    - Upload this sketch

  Created by Cristian Chitiva (cychitivav@unal.edu.co)
  Last updated on 6/4/2023
*/

#include <TinyWireS.h> // Import i2c library for slave device
#define ADDR 0x08      // Slave device address

void setup()
{
    pinMode(2, INPUT); // Set pin PB2 as input
    TinyWireS.begin(ADDR);
}

void loop()
{
    TinyWireS.send(analogRead(1));
    delay(100);
}