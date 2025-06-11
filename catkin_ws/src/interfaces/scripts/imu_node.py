#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Imu

class ImuNode:
    def __init__(self):
        self.publisher = rospy.Publisher('imu/data_raw', Imu, queue_size=10)
        self.rate = rospy.Rate(10)

    def run(self):
        rospy.loginfo('IMU node started')
        msg = Imu()
        while not rospy.is_shutdown():
            # TODO: populate IMU message fields from actual sensor
            self.publisher.publish(msg)
            self.rate.sleep()

if __name__ == '__main__':
    rospy.init_node('imu_node')
    node = ImuNode()
    node.run()
