#!/usr/bin/env python3
import argparse
import rospy
from interfaces.msg import WasteType


def main():
    parser = argparse.ArgumentParser(description="Publish WasteType messages")
    parser.add_argument('type', help='Waste type label')
    args = parser.parse_args()

    rospy.init_node('waste_type_publisher', anonymous=True)
    pub = rospy.Publisher('waste_type', WasteType, queue_size=10, latch=True)
    msg = WasteType(type=args.type)
    rospy.loginfo('Publishing %s', msg.type)
    pub.publish(msg)
    rospy.sleep(0.5)


if __name__ == '__main__':
    main()
