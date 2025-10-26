from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Declare arguments
    rviz_config = DeclareLaunchArgument(
        'rviz_config',
        default_value=PathJoinSubstitution([
            FindPackageShare('multifarmbot_bringup'), 'rviz', 'multifarmbot.rviz'
        ]),
        description='RViz config file'
    )

    # For each robot
    robots = ['robot1', 'robot2', 'robot3']
    nodes = []

    for robot in robots:
        urdf_path = PathJoinSubstitution([
            FindPackageShare('multifarmbot_description'), 'urdf', f'{robot}.urdf'
        ])

        robot_state_publisher = Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name=f'{robot}_robot_state_publisher',
            namespace=robot,
            parameters=[{'robot_description': urdf_path}],
            output='screen'
        )

        joint_state_publisher = Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name=f'{robot}_joint_state_publisher',
            namespace=robot,
            output='screen'
        )

        nodes.extend([robot_state_publisher, joint_state_publisher])

    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', LaunchConfiguration('rviz_config')],
        output='screen'
    )

    nodes.append(rviz)

    return LaunchDescription([rviz_config] + nodes)