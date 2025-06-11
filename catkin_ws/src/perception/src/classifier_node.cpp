#include <ros/ros.h>
#include <sensor_msgs/Image.h>
#include <std_msgs/String.h>
#include <cv_bridge/cv_bridge.h>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <NvInfer.h>
#include "perception/classifier.h"

namespace perception
{
Classifier::Classifier(const std::string& engine_path)
  : model_path_(engine_path)
{
  // In a real implementation, load TensorRT engine from model_path_
  // Here we keep it simple and do nothing if the file is missing
}

std::string Classifier::infer(const cv::Mat& image) const
{
  // Dummy inference based on mean intensity
  cv::Scalar mean = cv::mean(image);
  double intensity = (mean[0] + mean[1] + mean[2]) / 3.0;
  return intensity > 128.0 ? "bright" : "dark";
}
}

class ClassifierNode
{
public:
  ClassifierNode()
  {
    ros::NodeHandle pnh("~");
    std::string engine;
    pnh.param("engine_path", engine, std::string("model.trt"));
    classifier_.reset(new perception::Classifier(engine));
    image_sub_ = nh_.subscribe("image_raw", 1, &ClassifierNode::imageCb, this);
    class_pub_ = nh_.advertise<std_msgs::String>("/waste_class", 1);
  }

private:
  void imageCb(const sensor_msgs::ImageConstPtr& msg)
  {
    cv::Mat image = cv_bridge::toCvShare(msg, "bgr8")->image;
    std::string cls = classifier_->infer(image);
    std_msgs::String out;
    out.data = cls;
    class_pub_.publish(out);
  }

  ros::NodeHandle nh_;
  ros::Subscriber image_sub_;
  ros::Publisher class_pub_;
  std::unique_ptr<perception::Classifier> classifier_;
};

int main(int argc, char** argv)
{
  ros::init(argc, argv, "classifier_node");
  ClassifierNode node;
  ros::spin();
  return 0;
}
