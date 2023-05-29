#!/usr/bin/python
import rospy

from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

import numpy as np


class computer:
    def __init__(self):
        # Paremeters
        r = 0.0352
        # Right wheel
        alpha_right = -np.pi/2
        beta_right = np.pi
        l_right = 0.115
        # Left wheel
        alpha_left = np.pi/2
        beta_left = 0
        l_left = 0.115

        # Constraints
        J1 = np.array([(np.sin(alpha_right+beta_right),  -np.cos(alpha_right+beta_right),    -l_right*np.cos(beta_right)),
                       (np.sin(alpha_left+beta_left),    -np.cos(alpha_left+beta_left),      -l_left*np.cos(beta_left))])

        J2 = r*np.identity(2)

        # J2^-1 x J1
        self.jacobian = np.matmul(np.linalg.pinv(J2), J1)

        # Subscriber
        self.cmd_vel_subscriptor = rospy.Subscriber('/cmd_vel', Twist, self.callback_velocity)

        # Publishers
        self.pub_wheel_right = rospy.Publisher('/right_wheel_ctrl/command', Float64, queue_size=10)
        self.pub_wheel_left = rospy.Publisher('/left_wheel_ctrl/command', Float64, queue_size=10)

    def callback_velocity(self, cmd_vel):
        xiR = np.array([0, 0, 0], dtype=np.float)
        print(cmd_vel, '\n')

        sign = lambda x:  x/abs(x)

        # Velocity limits
        xiR[0] = cmd_vel.linear.x if abs(cmd_vel.linear.x) <= 1 else sign(cmd_vel.linear.x)
        xiR[1] = cmd_vel.linear.y if abs(cmd_vel.linear.y) <= 1 else sign(cmd_vel.linear.y)
        xiR[2] = cmd_vel.angular.z if abs(cmd_vel.angular.z) <= np.pi else sign(cmd_vel.angular.z)*np.pi


        phi = np.matmul(self.jacobian, xiR)

        msg_Float = Float64()
        msg_Float.data = phi[0]
        self.pub_wheel_right.publish(msg_Float)

        msg_Float.data = phi[1]
        self.pub_wheel_left.publish(msg_Float)


if __name__ == '__main__':
    rospy.init_node("Computer", anonymous=True)

    computer()
    rospy.spin()