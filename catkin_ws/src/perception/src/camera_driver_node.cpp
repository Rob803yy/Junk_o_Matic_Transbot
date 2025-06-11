#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/Image.h>
#include <opencv2/highgui/highgui.hpp>

int main(int argc, char** argv)
{
  ros::init(argc, argv, "camera_driver_node");
  ros::NodeHandle nh("~");

  int camera_id = 0;
  nh.param("camera_id", camera_id, 0);

  image_transport::ImageTransport it(nh);
  image_transport::Publisher pub = it.advertise("image_raw", 1);

  cv::VideoCapture cap(camera_id);
  if (!cap.isOpened())
  {
    ROS_ERROR("Failed to open camera %d", camera_id);
    return 1;
  }

  cv::Mat frame;
  ros::Rate rate(30.0);
  while (ros::ok())
  {
    cap >> frame;
    if (frame.empty())
    {
      ROS_WARN_THROTTLE(5, "Captured empty frame");
      rate.sleep();
      continue;
    }

    std_msgs::Header header;
    header.stamp = ros::Time::now();
    sensor_msgs::ImagePtr msg = cv_bridge::CvImage(header, "bgr8", frame).toImageMsg();
    pub.publish(msg);

    ros::spinOnce();
    rate.sleep();
  }
  return 0;
}
