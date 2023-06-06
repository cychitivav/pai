/*
  Battery voltage measurement using ATtiny85 ADC

  This code is for measuring battery voltage using ATtiny85 ADC and sending
  the value to master device via i2c. The address of the slave device is
  0x08 and can be changed in the code.

  Hardware Required:
  - ATtiny85

  Connections:
  - Connect battery voltage to PB3 (ADC3)
  - Connect SDA to PB0
  - Connect SCL to PB2
  - Connect GND to GND
  - Connect VCC to VCC

  Note: ATtiny85 only can read voltages up to VCC, so if you want to
  measure voltages higher than 5V, you need to use a voltage divider.

  Libraries Required (unzip and copy to documents/Arduino/libraries):
  - TinyWire:
    https://github.com/lucullusTheOnly/TinyWire

  Programming:
  - Connect ATtiny85 to Arduino Uno
  - Upload ArduinoISP sketch to Arduino Uno
  - Select "Arduino as ISP" programmer
  - Burn bootloader
  - Select "Arduino as ISP" programmer
  - Upload this sketch

  Created by Cristian Chitiva (cychitivav@unal.edu.co)
  Last updated on Jun/5/2023
*/

#include <TinyWire.h>
#define ADDR 0x08

void setup()
{
  pinMode(3, INPUT);                // Set PB3 (ADC3) as input
  TinyWire.begin(ADDR);          // config TinyWire library for I2C slave functionality
  TinyWire.onRequest(sendVoltage); // register a handler function in case of a request from a master
}

void loop()
{
}

void sendVoltage() // this function is called when the master requests data
{
  int voltage = analogRead(3); // Read voltage from PB3 (ADC3)

  TinyWire.send(voltage >> 8);   // Send high byte
  TinyWire.send(voltage & 0xFF); // Send low byte
}