cmake_minimum_required(VERSION 3.0.2)
project(perception)
find_package(catkin REQUIRED)
catkin_package()
include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  scripts/dummy_classifier.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
