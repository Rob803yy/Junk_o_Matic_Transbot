# Junk-o-Matic Transbot

[![Build Status](https://example.com/build.svg)](#)
[![Coverage Status](https://example.com/coverage.svg)](#)

This project adapts the Yahboom Transbot SE platform for autonomous litter collection.  It combines ROS Noetic packages, hardware integration guides, and design documents for a mobile robot capable of finding and binning lightweight waste in semi-structured outdoor environments.

## Build (ROS Noetic)
1. Install ROS Noetic on Ubuntu 20.04.
2. Create a workspace and clone this repository into `~/catkin_ws/src`.
3. Build the workspace:
   ```bash
   cd ~/catkin_ws
   catkin_make
   source devel/setup.bash
   ```

## Run
Launch the main bringup file after sourcing your workspace:
```bash
roslaunch transbot_bringup transbot.launch
```

## Repository Layout
```
├── 01.Introduction of Transbot      # Vendor overview
├── 02.Transbot assembly steps       # Mechanical build guide
├── 13.Code                          # Links to example code
├── docs/                            # Project documentation
└── README.md
```

See `docs/PM1.1.md` for the project purpose, scope, and reference materials.
