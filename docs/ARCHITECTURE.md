# Project Architecture Roadmap

This document outlines the six‑week integration plan for the upgraded Transbot system.

## Week 1 – Repository Cleanup
- Organize folders and remove redundant vendor examples.
- Add pre‑commit style checks and CI linting.

**Acceptance:** CI passes with no lint errors.

## Week 2 – Perception MVP
- Implement a minimal litter classifier and dataset.
- Integrate inference into the ROS stack.

**Acceptance:** Classifier reaches at least 80% accuracy on the test set.

## Week 3 – Manipulator Driver
- Bring up a ROS driver for the arm.
- Test basic pick routines in simulation.

**Acceptance:** Gazebo pick‑and‑place demo runs without collisions.

## Week 4 – Navigation Stub
- Launch a skeleton navigation stack with map and odometry sources.

**Acceptance:** Robot drives to three goal waypoints in Gazebo.

## Week 5 – Data Logging
- Record telemetry to rosbag and CSV for offline analysis.

**Acceptance:** Logs can be replayed and contain sensor and action topics.

## Week 6 – Design Review
- Evaluate system design and finalize backlog for the next phase.

**Acceptance:** Design review action items are signed off.
