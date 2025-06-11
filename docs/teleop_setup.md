# Teleop Setup

This package allows you to drive the robot in Gazebo or on real hardware using your keyboard.

## Build
```
cd catkin_ws
catkin_make
```

## Run
```
source devel/setup.bash
roslaunch teleop teleop.launch
```

Use the `W`, `A`, `S`, `D` keys to move the robot and `CTRL-C` to stop.
