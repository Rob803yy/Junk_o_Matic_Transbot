cmake_minimum_required(VERSION 3.0.2)
project(perception)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  image_transport
  cv_bridge
  sensor_msgs
  std_msgs
)

find_package(OpenCV REQUIRED)
find_library(TENSORRT_LIB nvinfer)

catkin_package(
  INCLUDE_DIRS include
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
)

add_executable(camera_driver_node src/camera_driver_node.cpp)
target_link_libraries(camera_driver_node
  ${catkin_LIBRARIES}
  ${OpenCV_LIBRARIES}
)

add_executable(classifier_node src/classifier_node.cpp)
target_link_libraries(classifier_node
  ${catkin_LIBRARIES}
  ${OpenCV_LIBRARIES}
  ${TENSORRT_LIB}
)

if(CATKIN_ENABLE_TESTING)
  find_package(rostest REQUIRED)
  catkin_add_gtest(classifier_test test/classifier_test.cpp)
  target_link_libraries(classifier_test ${catkin_LIBRARIES} ${OpenCV_LIBRARIES})
endif()
