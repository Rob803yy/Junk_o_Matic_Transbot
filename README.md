# Junk-o-Matic Transbot

This repository collects open-source ROS packages and reference material for a Transbot-based waste collection prototype. Most of the vendor documentation has been preserved alongside our own ROS workspace so the system can be rebuilt entirely offline.

## Building the ROS workspace

The main ROS workspace lives in `catkin_ws/`. Build it using standard `catkin_make` commands:

```bash
cd catkin_ws
rosdep install --from-paths src -r -y
catkin_make
source devel/setup.bash
```

After sourcing `devel/setup.bash`, you can run any of the packages with `rosrun` or `roslaunch` as usual.

## Repository layout

```
catkin_ws/        - Catkin workspace with core packages
about_hardware/   - Datasheets and hardware manuals
hardware/manuals/ - Additional vendor manuals
vendor_libs/      - Archived vendor Python libraries
docs/             - Project docs
  └── vendor-lessons/ - Vendor tutorial PDFs
```

The `ros_*` folders provide additional course material such as lidar demos and robotic arm examples.

### Vendor lessons and hardware manuals

Detailed step-by-step vendor lessons are stored in `docs/vendor-lessons/`. Hardware datasheets, interface documents and other manuals can be found under `about_hardware/` and `hardware/manuals/`.
