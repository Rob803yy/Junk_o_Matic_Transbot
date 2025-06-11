#!/usr/bin/env python
import unittest
import rospy
import actionlib
from manipulation.msg import PickPlaceAction, PickPlaceGoal
from gazebo_msgs.srv import SpawnModel, DeleteModel
from geometry_msgs.msg import Pose
import rospkg

class PickPlaceTest(unittest.TestCase):
    def test_pick_place(self):
        rospy.wait_for_service('/gazebo/spawn_sdf_model')
        rospy.wait_for_service('/gazebo/delete_model')
        spawn = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
        delete = rospy.ServiceProxy('/gazebo/delete_model', DeleteModel)

        pkg = rospkg.RosPack().get_path('manipulation')
        with open(pkg + '/models/box.sdf', 'r') as f:
            sdf = f.read()
        pose = Pose()
        spawn('test_box', sdf, '', pose, 'world')

        client = actionlib.SimpleActionClient('pick_place', PickPlaceAction)
        client.wait_for_server()
        successes = 0
        trials = 5
        for i in range(trials):
            goal = PickPlaceGoal(bin_id=i)
            client.send_goal(goal)
            client.wait_for_result()
            result = client.get_result()
            if result and result.success:
                successes += 1
        delete('test_box')
        ratio = float(successes) / trials
        self.assertGreaterEqual(ratio, 0.8)

if __name__ == '__main__':
    rospy.init_node('test_pick_place')
    import rostest
    rostest.rosrun('manipulation', 'pick_place_test', PickPlaceTest)
