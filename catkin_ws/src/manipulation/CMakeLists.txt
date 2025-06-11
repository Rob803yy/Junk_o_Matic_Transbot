cmake_minimum_required(VERSION 3.0.2)
project(manipulation)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  actionlib
  actionlib_msgs
  control_msgs
  trajectory_msgs
  geometry_msgs
  gazebo_msgs
  message_generation
)

add_action_files(
  DIRECTORY action
  FILES PickPlace.action
)

generate_messages(
  DEPENDENCIES actionlib_msgs geometry_msgs std_msgs
)

catkin_package(
  CATKIN_DEPENDS roscpp actionlib actionlib_msgs control_msgs trajectory_msgs geometry_msgs message_runtime
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(arm_interface_node src/arm_interface_node.cpp)
add_dependencies(arm_interface_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(arm_interface_node ${catkin_LIBRARIES})

add_executable(pick_place_server src/pick_place_server.cpp)
add_dependencies(pick_place_server ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(pick_place_server ${catkin_LIBRARIES})

if(CATKIN_ENABLE_TESTING)
  find_package(rostest REQUIRED)
  add_rostest(test/pick_place.test)
endif()

install(TARGETS arm_interface_node pick_place_server
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY models
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
