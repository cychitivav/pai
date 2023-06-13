#!/usr/bin/python
import sys

import pigpio
import rospy
from std_msgs.msg import Bool, Float64


class Motor():
    MAX_SPEED = 100#160 * (2*3.14/60)  # 160 rpm

    def __init__(self, pwm_pin: int, dir_pin: int, pi: pigpio.pi):
        self.pi = pi

        self.pwm_pin = pwm_pin
        self.dir_pin = dir_pin

        # Set range to 0-100
        self.pi.set_PWM_range(self.pwm_pin, 100)

        # Set frequency to 8kHz
        self.pi.set_PWM_frequency(self.pwm_pin, 8000)

        self.speed = 0

    def set_speed(self, speed: float):
        rate = rospy.Rate(120)  # 120hz

        step = 2*self.MAX_SPEED/100 * (1 if speed > self.speed else -1)
        instant_speed = self.speed
        while abs(instant_speed - speed) > abs(step):
            instant_speed += step

            if instant_speed < 0:
                abs_speed = -instant_speed
                dir_value = 1
            else:
                abs_speed = instant_speed
                dir_value = 0

            if abs_speed > self.MAX_SPEED:
                abs_speed = self.MAX_SPEED
            
            # Set direction
            self.pi.write(self.dir_pin, dir_value)
            # Set duty cycle to speed
            self.pi.set_PWM_dutycycle(self.pwm_pin, abs_speed)

            rospy.loginfo("Motor speed: " + str(instant_speed))

            rate.sleep()

            self.speed = speed
            rospy.logwarn("Motor speed: " + str(self.speed))


class DualMotorDriver():

    def __init__(self, host='localhost', pin_out: dict = {'FAULT': 23, 'PWM2': 24, 'PWM1': 12, 'DIR2': 16, 'DIR1': 20, 'EN': 21}):
        rospy.init_node("Driver", anonymous=True)

        # Initialize pigpio
        self.pi = pigpio.pi(host)
        if not self.pi.connected:
            rospy.signal_shutdown("Pigpio not connected, run `sudo pigpiod` or specify host")
            exit()

        # Initialize motors
        self.motorA = Motor(pin_out['PWM1'], pin_out['DIR1'], self.pi)
        self.motorB = Motor(pin_out['PWM2'], pin_out['DIR2'], self.pi)

        # Initialize fault pin
        self.pin_FAULT = pin_out['FAULT']
        self.pi.set_pull_up_down(self.pin_FAULT, pigpio.PUD_UP)  # make sure FAULT is pulled up

        # Initialize enable pin
        self.pin_EN = pin_out['EN']
        self.pi.write(self.pin_EN, 0)  # enable drivers by default
        self.pi.callback(self.pin_FAULT, pigpio.FALLING_EDGE, self.get_fault) # Check for faults

        # Subscriber
        self.sub_front_right = rospy.Subscriber(
            '/motor_A_ctrl/command', Float64, self.set_speed_M1)
        self.sub_front_left = rospy.Subscriber(
            '/motor_B_ctrl/command', Float64, self.set_speed_M2)

        # Publishers
        self.pub_fault_warning = rospy.Publisher('/fault_warning', Bool, queue_size=10)

        rospy.loginfo("Driver " + rospy.get_name() + " started")
        rospy.loginfo("Driver " + rospy.get_name() + " pins: " + str(pin_out))

        if rospy.is_shutdown():
            self.pi.stop()


    def set_speed_M1(self, Float64_msg):
        m1_speed = Float64_msg.data
        self.motorA.set_speed(m1_speed)
        rospy.logdebug("Motor 1 speed:" + str(m1_speed))

    def set_speed_M2(self, Float64_msg):
        m2_speed = Float64_msg.data
        self.motorB.set_speed(m2_speed)
        rospy.logdebug("motor 2 speed:" + str(m2_speed))

    def get_fault(self):
        rospy.signal_shutdown("Motor driver fault")

    def enable(self):
        rospy.logwarn("Motors enabled")
        self.pi.write(self.pin_EN, 0)

    def disable(self):
        rospy.logwarn("Motors disabled")
        self.pi.write(self.pin_EN, 1)


if __name__ == '__main__':
    if len(sys.argv) > 2:
        pins = rospy.get_param(sys.argv[2])
        DualMotorDriver(host=sys.argv[1], pin_out=pins)
    else: 
        DualMotorDriver()
    rospy.spin()
