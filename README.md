# Multifarmbot

This is the multifarmbot ROS2 repository for multi-robot farming applications.

## Setup

1. Install ROS2 (e.g., Humble Hawksbill) following the [official guide](https://docs.ros.org/en/humble/Installation.html).

2. Clone this repository:
   ```
   git clone https://github.com/tomo1000cmd/multifarmbot.git
   cd multifarmbot
   ```

3. Build the workspace:
   ```
   colcon build
   ```

4. Source the setup:
   ```
   source install/setup.bash
   ```

## Packages

- `multifarmbot_agents`: Robot agent behaviors
- `multifarmbot_bringup`: System bringup and launch files
- `multifarmbot_control`: Control algorithms
- `multifarmbot_description`: Robot descriptions (URDF, etc.)
- `multifarmbot_localization`: Localization and mapping
- `multifarmbot_msgs`: Custom messages, services, actions
- `multifarmbot_navigation`: Navigation and path planning
- `multifarmbot_ui`: User interface components

## Usage

Run example launch files or nodes as needed. Refer to individual package READMEs for details.