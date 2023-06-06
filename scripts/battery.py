#!/usr/bin/python
import rospy

from sensor_msgs.msg import BatteryState
from pai.srv import CalibrateBattery, CalibrateBatteryResponse

import pigpio


class Battery(pigpio.pi):
    def __init__(self):
        rospy.init_node('Battery', anonymous=True)

        super().__init__()
        if not self.connected:
            rospy.signal_shutdown("Pigpio not connected, run 'sudo pigpiod'")

        self.ATtiny85 = self.i2c_open(1, 0x08) # Open i2c bus 1, slave address 0x08 (ATtiny85)
        self.factor = 24.6/435 # Calibration factor

        self.pub = rospy.Publisher('/battery', BatteryState, queue_size=10)
        self.ser = rospy.Service('/calibrate_battery', CalibrateBattery, self.update_calibration)
        
        msg = BatteryState()

        msg.temperature = float('nan')
        msg.current = float('nan')
        msg.charge = float('nan')
        msg.capacity = float('nan')
        msg.design_capacity = 7.8

        msg.power_supply_status = BatteryState.POWER_SUPPLY_STATUS_DISCHARGING
        msg.power_supply_health = BatteryState.POWER_SUPPLY_HEALTH_UNKNOWN
        msg.power_supply_technology = BatteryState.POWER_SUPPLY_TECHNOLOGY_LION

        msg.present = True

        msg.cell_voltage = [float('nan')]*18
        msg.cell_temperature = [float('nan')]*18

        msg.serial_number = '05638'
        msg.location = 'Base'

        rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            msg.header.stamp = rospy.Time.now()

            msg.voltage = self.get_voltage()
            msg.percentage = msg.voltage/25.2

            self.pub.publish(msg)
            rate.sleep()

    def get_voltage(self):
        # Read int(2 bytes) from slave when it sends data
        (_, data) = self.i2c_read_device(self.ATtiny85, 2)
        # Convert bytes to float
        data = int.from_bytes(data, byteorder='big') * self.factor

        return data

    def update_calibration(self, req):
        # Get current battery number
        (_, data) = self.i2c_read_device(self.ATtiny85, 2)
        data = int.from_bytes(data, byteorder='big')

        # Update calibration factor
        if data:
            self.factor = req.voltage / data

            rospy.loginfo("Battery voltage: %f", self.get_voltage())
            rospy.loginfo("Battery percentage: %f", self.get_voltage()/25.2)
        else:
            rospy.logerr("Battery number is 0, check battery connection")

        return CalibrateBatteryResponse()



if __name__ == '__main__':
    Battery()
    rospy.spin()