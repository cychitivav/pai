#!/usr/bin/python
import sys

import pigpio
import rospy
from std_msgs.msg import Float64


class MotorDriver():
    MAX_SPEED = 100  # 160 * (2*3.14/60)  # 160 rpm

    def __init__(self, host='localhost', pin_out: dict = {'EN': 18, 'PWM_R': 23, 'PWM_L': 24}):
        rospy.init_node("Driver", anonymous=True)

        # Initialize pigpio
        self.pi = pigpio.pi(host)
        if not self.pi.connected:
            rospy.signal_shutdown("Pigpio not connected, run `sudo pigpiod` or specify host")
            exit()

        # Set PWM pins
        # Initialize pins
        self.pwm_forward = pin_out['PWM_L']
        self.pwm_reverse = pin_out['PWM_R']

        # Set range to 0-100
        self.pi.set_PWM_range(self.pwm_forward, 10000)
        self.pi.set_PWM_range(self.pwm_reverse, 10000)

        # Set frequency to 8kHz (pigpiod by default mode 5)
        self.pi.set_PWM_frequency(self.pwm_forward, 8000)
        self.pi.set_PWM_frequency(self.pwm_reverse, 8000)

        # Turn off motors
        self.pi.set_PWM_dutycycle(self.pwm_forward, 0)
        self.pi.set_PWM_dutycycle(self.pwm_reverse, 0)

        # Initialize enable pin
        self.pin_EN = pin_out['EN']
        self.pi.write(self.pin_EN, 1)  # enable drivers by default

        # Subscriber
        self.sub_front_right = rospy.Subscriber('/motor_ctrl/command', Float64, self.set_speed)

        rospy.loginfo("Driver " + rospy.get_name() + " started")
        rospy.loginfo("Driver " + rospy.get_name() + " pins: " + str(pin_out))

        rospy.on_shutdown(self.stop)

    def set_speed(self, Float64_msg):
        speed = Float64_msg.data

        if abs(speed) > self.MAX_SPEED:
            speed = self.MAX_SPEED * speed / abs(speed)

        if speed > 0:  # Turn left (forward)
            self.pi.set_PWM_dutycycle(self.pwm_reverse, 0)
            rospy.sleep(0.001)
            self.pi.set_PWM_dutycycle(self.pwm_forward, speed*100)
        else:  # Turn right (reverse)
            self.pi.set_PWM_dutycycle(self.pwm_forward, 0)
            rospy.sleep(0.001)
            self.pi.set_PWM_dutycycle(self.pwm_reverse, -speed*100)

        rospy.logdebug("Motor " + rospy.get_name() + " speed:" + str(speed))

    def enable(self):
        rospy.logwarn("Motor " + rospy.get_name() + " enabled")
        self.pi.write(self.pin_EN, 1)

    def disable(self):
        rospy.logwarn("Motor " + rospy.get_name() + " disabled")
        self.pi.write(self.pin_EN, 0)

    def stop(self):
        self.disable()
        self.set_speed(Float64(0))
        self.pi.stop()


if __name__ == '__main__':
    if len(sys.argv) > 2:
        pins = rospy.get_param(sys.argv[2])
        MotorDriver(host=sys.argv[1], pin_out=pins)
    else:
        MotorDriver()
    rospy.spin()
