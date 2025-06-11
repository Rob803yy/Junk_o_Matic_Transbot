# Navigation Demo

This example shows how to run a minimal navigation stack using `move_base` with a mock map in Gazebo.

## Build the workspace

```bash
cd catkin_ws
catkin_make
source devel/setup.bash
```

## Run in Gazebo

```bash
roslaunch navigation waypoint_nav.launch
```

The launch file starts a map server, AMCL localization, the `move_base` node and a simple waypoint follower. The waypoints loaded from `config/waypoints.yaml` demonstrate sending a sequence of goals for the robot in simulation.
