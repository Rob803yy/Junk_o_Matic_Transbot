#!/usr/bin/env python3
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Quaternion
import tf

def quaternion_from_yaw(yaw):
    q = tf.transformations.quaternion_from_euler(0, 0, yaw)
    return Quaternion(*q)

def main():
    rospy.init_node('waypoint_nav')
    waypoints = rospy.get_param('~waypoints', [])
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    rospy.loginfo('Waiting for move_base action server...')
    client.wait_for_server()
    for wp in waypoints:
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = 'map'
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = wp['x']
        goal.target_pose.pose.position.y = wp['y']
        goal.target_pose.pose.orientation = quaternion_from_yaw(wp.get('yaw', 0.0))
        rospy.loginfo('Sending waypoint: %s', wp)
        client.send_goal(goal)
        client.wait_for_result()
        rospy.sleep(1.0)
    rospy.loginfo('All waypoints reached')

if __name__ == '__main__':
    main()
