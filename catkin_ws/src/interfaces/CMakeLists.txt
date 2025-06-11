cmake_minimum_required(VERSION 3.0.2)
project(interfaces)

find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(${PROJECT_NAME}_node src/interfaces_node.cpp)
target_link_libraries(${PROJECT_NAME}_node ${catkin_LIBRARIES})

install(TARGETS ${PROJECT_NAME}_node
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
