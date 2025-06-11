#include <ros/ros.h>
#include <actionlib/server/simple_action_server.h>
#include <manipulation/PickPlaceAction.h>
#include <geometry_msgs/Pose.h>

class PickPlaceServer
{
public:
  PickPlaceServer()
    : as_(nh_, "pick_place", boost::bind(&PickPlaceServer::execute, this, _1), false)
  {
    as_.start();
    ROS_INFO("PickPlace action server started");
  }

  void execute(const manipulation::PickPlaceGoalConstPtr& goal)
  {
    manipulation::PickPlaceFeedback fb;
    fb.grasp_pose.orientation.w = 1.0; // dummy pose
    as_.publishFeedback(fb);
    manipulation::PickPlaceResult res;
    res.success = true; // always succeed for placeholder
    as_.setSucceeded(res);
  }

private:
  ros::NodeHandle nh_;
  actionlib::SimpleActionServer<manipulation::PickPlaceAction> as_;
};

int main(int argc, char** argv)
{
  ros::init(argc, argv, "pick_place_server");
  PickPlaceServer server;
  ros::spin();
  return 0;
}
