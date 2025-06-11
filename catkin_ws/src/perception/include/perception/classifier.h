#ifndef PERCEPTION_CLASSIFIER_H
#define PERCEPTION_CLASSIFIER_H

#include <string>
#include <opencv2/core.hpp>

namespace perception
{
class Classifier
{
public:
  explicit Classifier(const std::string& engine_path="");
  std::string infer(const cv::Mat& image) const;
private:
  std::string model_path_;
};
}

#endif // PERCEPTION_CLASSIFIER_H
