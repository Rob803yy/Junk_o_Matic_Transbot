#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String

class DummyClassifier:
    def __init__(self):
        self.publisher = rospy.Publisher('/perception/classification', String, queue_size=10)
        self.subscriber = rospy.Subscriber('/camera/image_raw', Image, self.callback)

    def callback(self, msg):
        # Always publish the same label as a placeholder
        result = String(data='unknown object')
        self.publisher.publish(result)

if __name__ == '__main__':
    rospy.init_node('dummy_classifier')
    DummyClassifier()
    rospy.spin()
