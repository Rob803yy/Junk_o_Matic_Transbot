#include <gtest/gtest.h>
#include <opencv2/core.hpp>
#include "perception/classifier.h"

TEST(ClassifierTest, Accuracy)
{
  perception::Classifier cls("");
  int correct = 0;
  for (int i = 0; i < 20; ++i)
  {
    bool bright = (i % 2) == 0;
    cv::Mat img(10, 10, CV_8UC3, cv::Scalar(bright ? 255 : 0,
                                            bright ? 255 : 0,
                                            bright ? 255 : 0));
    std::string gt = bright ? "bright" : "dark";
    if (cls.infer(img) == gt)
      ++correct;
  }
  EXPECT_GE(correct, 18); // >=90%
}

int main(int argc, char **argv)
{
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
