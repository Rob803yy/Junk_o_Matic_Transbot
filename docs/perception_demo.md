# Perception Demo

This demo runs a simple node that subscribes to camera images and publishes a dummy classification result.

## Running the Demo

1. Build the workspace if you haven't already:
   ```bash
   cd ~/catkin_ws
   catkin_make
   ```
2. Launch the demo:
   ```bash
   roslaunch perception perception_demo.launch
   ```
   The node listens on `/camera/image_raw` and publishes a constant label on `/perception/classification`.
