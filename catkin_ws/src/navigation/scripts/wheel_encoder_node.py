#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry

class WheelEncoderNode:
    def __init__(self):
        self.publisher = rospy.Publisher('wheel/odometry', Odometry, queue_size=10)
        self.rate = rospy.Rate(10)

    def run(self):
        rospy.loginfo('Wheel encoder node started')
        msg = Odometry()
        while not rospy.is_shutdown():
            # TODO: compute odometry from encoder ticks
            self.publisher.publish(msg)
            self.rate.sleep()

if __name__ == '__main__':
    rospy.init_node('wheel_encoder_node')
    node = WheelEncoderNode()
    node.run()
