#include <ros/ros.h>
int main(int argc, char** argv){
  ros::init(argc, argv, "interfaces_node");
  ros::NodeHandle nh;
  ROS_INFO("Interfaces node running");
  ros::Rate r(1);
  while (ros::ok()){
    ros::spinOnce();
    r.sleep();
  }
  return 0;
}
