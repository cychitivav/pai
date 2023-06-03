# Python library for the Pololu Dual MAX14870 Motor Driver for Raspberry Pi

Version: 1.0.1<br>
Release Date: 2018-04-03<br>
[www.pololu.com](https://www.pololu.com/)

## Summary

This library runs on the [Raspberry Pi](https://www.pololu.com/product/2759)
(Model B+ or newer) and provides functions for controlling both channels of the
[Pololu Dual MAX14870 Motor Driver for Raspberry Pi](https://www.pololu.com/product/3758).
This library supports both Python 2 and Python 3.

## Getting Started

### Installation

This library depends on [pigpio](http://abyz.me.uk/rpi/pigpio/), and the
instructions below explain how to set it up.

These instructions assume you are using Raspbian, Debian, or some other
distribution that provides the `apt` command for managing packages. If you do
not have `apt`, you will need to use a different method to install the required
packages.

These instructions also assume you will use Python 2.  If you want to use
Python 3, you will need to:
* install the `python3-pigpio` package instead of `python-pigpio`
  (it is okay to install both)
* use the `python3` command instead of `python` for running Python scripts

First, to download and install pigpio and its Python module, run:

```
sudo apt install python-pigpio
```

Then, to start the `pigpiod` daemon, run:

```
sudo systemctl start pigpiod
```

Optionally, to automatically start the daemon every time your Raspberry Pi
boots, you can also run:

```
sudo systemctl enable pigpiod
```

Finally, to download and install the dual_max14870_rpi library, run:

```
git clone https://github.com/pololu/dual-max14870-motor-driver-rpi
cd dual-max14870-motor-driver-rpi
sudo python setup.py install
```

### Running the example program

This library comes with an example program that drives each motor in both
directions.  To run the example, navigate to the
dual-max14870-motor-driver-rpi directory and run:

```
python example.py
```

## Library reference

This library uses ultrasonic 20&nbsp;kHz PWM to drive the motors.

Motor speeds in this library are represented as numbers between **-480** and
**480** (inclusive).  A speed of 0 corresponds to braking.  Positive speeds
correspond to current flowing from M1A/M2A to M1B/M2B, while negative speeds
correspond to current flowing in the other direction.

The library can be imported into a Python program with the following line:

```
from dual_max14870_rpi import motors, MAX_SPEED
```

After importing the library, you can use the functions below to enable the motors
and set motor speeds:

* `motors.enable()`: Enable the motor drivers.
* `motors.disable()`: Disable the motor drivers.
* `motors.setSpeeds(m1_speed, m2_speed)`: Set speed and direction for both motor 1 and motor 2.
* `motors.motor1.setSpeed(speed)`: Set speed and direction for motor 1.
* `motors.motor2.setSpeed(speed)`: Set speed and direction for motor 2.
* `motors.getFault()`: Returns `True` if there is a motor driver fault, `False`
  if no fault.

For convenience, a constant called `MAX_SPEED` (which is equal to 480) is
available on all the objects provided by this library.  You can access it
directly by just writing `MAX_SPEED` if you imported it as shown above, or it
can be accessed in the following ways:

* `motors.MAX_SPEED`
* `motors.motor1.MAX_SPEED`
* `motors.motor2.MAX_SPEED`

If you are controlling multiple motor drivers, you might prefer to import the
library using `import dual_max14870_rpi`, which requires the commands listed
above to be prefixed with `dual_max14870_rpi.`.

## Version history

* 1.0.1 (2018-04-03): Improved error behavior and exception handling.
* 1.0.0 (2018-03-30): Original release.
