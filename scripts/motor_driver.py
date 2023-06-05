#!/usr/bin/python
import rospy

from geometry_msgs.msg import Twist
from std_msgs.msg import Float64, Bool

import numpy as np

#is_sim = rospy.get_param('sim')
#if not is_sim:
from dual_max14870_rpi import DualMotorDriver

#PWM1_pin = rospy.get_param('PWM1_pin')
#PWM2_pin = rospy.get_param('PWM2_pin')
#dir1_pin = rospy.get_param('dir1_pin')
#dir2_pin = rospy.get_param('dir2_pin')
#enable_pin = rospy.get_param('enable_pin')
#fault_pin = rospy.get_param('fault_pin')
    
    
    


class Driver(DualMotorDriver):
    def __init__(self):
       

        # Subscriber
        self.sub_front_right = rospy.Subscriber(
            '/front_wheel_ctrl/command', Float64, self.setSpeedsRosWrapper)
        #self.sub_front_left = rospy.Subscriber(
        #    '/back_wheel_ctrl/command', Float64, self.callback_velocity)
        
        # Publishers
        self.pub_fault_warning = rospy.Publisher('/fault_warning', Bool, queue_size=10)
        
        

    def setSpeedsRosWrapper(self, Float64_msg):
        m1_speed = Float64_msg.data
        m2_speed = Float64_msg.data
            
        self.setSpeeds(self, m1_speed, m2_speed)

    def getFaultRosWrapper(self):
        Bool_msg = Bool
        Bool_msg.data = self.getFault()
        self.pub_fault_warning(Bool_msg)
        


if __name__ == '__main__':
    rospy.init_node("Computer", anonymous=True)
    Driver()
    rospy.spin()
