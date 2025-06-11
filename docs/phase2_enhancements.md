# Phase 2 Enhancements

This phase introduces hardware interface nodes and message definitions for new sensors and actuators.

## Wheel Encoder Node (`navigation` package)
- **Node Name**: `wheel_encoder_node`
- **Publishes**: `nav_msgs/Odometry` on `wheel/odometry`
- **Parameters**:
  - `wheel_radius` (double): radius of the drive wheels in meters.
  - `ticks_per_rev` (int): encoder ticks per wheel revolution.

## IMU Node (`interfaces` package)
- **Node Name**: `imu_node`
- **Publishes**: `sensor_msgs/Imu` on `imu/data_raw`
- **Parameters**:
  - `port` (string): serial device for the IMU.
  - `frame_id` (string): TF frame for the IMU data.

## Arm Driver Node (`manipulation` package)
- **Node Name**: `arm_driver_node`
- **Subscribes**: `std_msgs/String` on `arm/command`
- **Parameters**:
  - `baudrate` (int): serial speed for the arm controller.
  - `port` (string): serial device for the arm.

These stubs provide a starting point for integrating real hardware drivers and should be expanded with actual sensor handling logic.
