#include <ros/ros.h>
#include <actionlib/client/simple_action_client.h>
#include <control_msgs/FollowJointTrajectoryAction.h>
#include <trajectory_msgs/JointTrajectory.h>

class ArmInterface
{
public:
  ArmInterface()
    : ac_("/arm_controller/follow_joint_trajectory", true)
  {
    ros::NodeHandle nh;
    sub_ = nh.subscribe("trajectory", 1, &ArmInterface::trajCallback, this);
    ROS_INFO("Waiting for joint_trajectory_controller...");
    ac_.waitForServer();
    ROS_INFO("Connected to controller");
  }

  void trajCallback(const trajectory_msgs::JointTrajectory::ConstPtr& msg)
  {
    control_msgs::FollowJointTrajectoryGoal goal;
    goal.trajectory = *msg;
    ac_.sendGoal(goal);
  }

private:
  actionlib::SimpleActionClient<control_msgs::FollowJointTrajectoryAction> ac_;
  ros::Subscriber sub_;
};

int main(int argc, char** argv)
{
  ros::init(argc, argv, "arm_interface_node");
  ArmInterface iface;
  ros::spin();
  return 0;
}
