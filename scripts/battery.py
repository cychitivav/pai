#!/usr/bin/python
import rospy

from std_msgs.msg import Float64, BatteryState, Float32, String
from cob_srvs.srv import SetFloat64, SetFloat64Request  

import pigpio


class Battery(pigpio.pi):
    def __init__(self):
        rospy.init_node('Battery', anonymous=True)

        super().__init__()
        if not self.connected:
            rospy.signal_shutdown("Pigpio not connected")

        self.i2c_open(1, 0x08) # Open i2c bus 1, slave address 0x08 (ATtiny85)
        self.factor = 24.6/4350 # Calibration factor

        self.pub = rospy.Publisher('/battery', Float64, queue_size=10)
        self.ser = rospy.Service('calibrate_battery', SetFloat64, self.update_calibration)
        
        msg = BatteryState()

        msg.temperature = Float32("NaN")
        msg.current = Float32("NaN")
        msg.charge = Float32("NaN")
        msg.capacity = Float32("NaN")
        msg.design_capacity = Float32(7.8)

        msg.PowerSupplyStatus = BatteryState.POWER_SUPPLY_STATUS_DISCHARGING
        msg.PowerSupplyHealth = BatteryState.POWER_SUPPLY_HEALTH_UNKNOWN
        msg.PowerSupplyTechnology = BatteryState.POWER_SUPPLY_TECHNOLOGY_LION

        msg.present = True

        msg.cell_voltage = [Float32("NaN")]*18
        msg.cell_temperature = [Float32("NaN")]*18

        msg.SerialNumber = String("05638")
        msg.Location = String("Base")

        rate = rospy.Rate(1/60)
        while not rospy.is_shutdown():
            voltage = self.get_voltage()
            msg.voltage = Float32(voltage)
            msg.percentage = Float32(voltage/25.2)

            self.pub.publish(msg)
            rate.sleep()

    def get_voltage(self):
        # Read int(2 bytes) from slave when it sends data
        (_, data) = self.i2c_read_device(h, 2)
        # Convert data to int
        data = int.from_bytes(data, byteorder='big') * self.factor

        return data

    def update_calibration(self, req):
        # Get current battery number
        (_, data) = self.i2c_read_device(h, 2)
        data = int.from_bytes(data, byteorder='big')

        # Update calibration factor
        self.factor = req.data / data


if __name__ == '__main__':
    Battery()
    rospy.spin()