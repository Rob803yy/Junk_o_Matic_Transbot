cmake_minimum_required(VERSION 3.0.2)
project(manipulation)
find_package(catkin REQUIRED)
catkin_package()
include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  scripts/arm_driver_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
