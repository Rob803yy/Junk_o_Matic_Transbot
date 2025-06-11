#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

class ArmDriverNode:
    def __init__(self):
        self.command_sub = rospy.Subscriber('arm/command', String, self.command_cb)
        rospy.loginfo('Arm driver node initialized')

    def command_cb(self, msg):
        # TODO: send command to physical arm controller
        rospy.loginfo('Received arm command: %s', msg.data)

if __name__ == '__main__':
    rospy.init_node('arm_driver_node')
    node = ArmDriverNode()
    rospy.spin()
