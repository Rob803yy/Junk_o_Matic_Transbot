#!/usr/bin/env python3
import argparse
import rospy
from interfaces.msg import BinID


def main():
    parser = argparse.ArgumentParser(description="Publish BinID messages")
    parser.add_argument('id', type=int, help='Bin identifier')
    args = parser.parse_args()

    rospy.init_node('bin_id_publisher', anonymous=True)
    pub = rospy.Publisher('bin_id', BinID, queue_size=10, latch=True)
    msg = BinID(id=args.id)
    rospy.loginfo('Publishing bin id: %d', msg.id)
    pub.publish(msg)
    rospy.sleep(0.5)


if __name__ == '__main__':
    main()
