# Multifarmbot Description

This package contains the robot descriptions for the multifarmbot project.

## Robots

- **Farmbot**: A four-wheel agricultural robot with all-wheel steering capability.
  - Supports namespacing for multiple instances in simulation.
  - URDF files: `robot1.urdf`, `robot2.urdf`, `robot3.urdf` (generated from `farmbot.xacro`).

## Usage

To use in simulation:
- Spawn each robot with a unique namespace (e.g., `/robot1`, `/robot2`, `/robot3`).
- Use the URDF files located in `share/multifarmbot_description/urdf/`.

## Customization

Modify `farmbot.xacro` to change robot parameters, then regenerate URDFs with:
```
xacro farmbot.xacro robot_name:=<name> > <name>.urdf
```