cmake_minimum_required(VERSION 3.0.2)
project(navigation)
find_package(catkin REQUIRED)
catkin_package()
include_directories(
  ${catkin_INCLUDE_DIRS}
)

if(CATKIN_ENABLE_TESTING)
  find_package(rostest REQUIRED)
  add_rostest(test/test_basic.test)
endif()
