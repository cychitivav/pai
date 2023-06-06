#!/usr/bin/python
import rospy
import rosparam

from geometry_msgs.msg import Twist
from std_msgs.msg import Float64, Bool

import numpy as np

from dual_max14870_rpi import DualMotorDriver

pin = rospy.get_param(rospy.get_name(), {'FAULT':23, 'PWM2':24, 'PWM1':12, 'DIR2':16, 'DIR1':20, 'EN': 21})

class Driver(DualMotorDriver):
    def __init__(self):
        super().__init__(pin['PWM1'],pin['DIR1'],pin['PWM2'],pin['DIR2'],pin['FAULT'],pin['EN'])

        # Subscriber
        self.sub_front_right = rospy.Subscriber(
            '/wheel_A_ctrl/command', Float64, self.setSpeedM1RosWrapper)
        self.sub_front_left = rospy.Subscriber(
            '/wheel_B_ctrl/command', Float64, self.setSpeedM2RosWrapper)
        
        # Publishers
        self.pub_fault_warning = rospy.Publisher('/fault_warning', Bool, queue_size=10)
        rospy.loginfo("driver start")
        rospy.loginfo("driver pinout: " +str(pin_out))
        

    def setSpeedM1RosWrapper(self, Float64_msg):
        m1_speed = Float64_msg.data
        self.motor1.setSpeed(m1_speed)
        rospy.logdebug("motor 1 speed:" + str(m1_speed))       
    
    def setSpeedM2RosWrapper(self, Float64_msg):
        m2_speed = Float64_msg.data
        self.motor2.setSpeed(m2_speed) 
        rospy.logdebug("motor 2 speed:" + str(m2_speed))

    def getFaultRosWrapper(self):
        Bool_msg = Bool
        Bool_msg.data = self.getFault()
        rospy.logwarn("driver fault detected")
        self.pub_fault_warning(Bool_msg)

        


if __name__ == '__main__':
    rospy.init_node("Driver", anonymous=True)
    Driver()
    rospy.spin()
