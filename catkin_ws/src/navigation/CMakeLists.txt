cmake_minimum_required(VERSION 3.0.2)
project(navigation)
find_package(catkin REQUIRED)
catkin_package()
include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  scripts/wheel_encoder_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
