from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='cvxcv',
            executable='Node1.py',
            name='node1'
        ),

        # customize launch file below

        # end launch file customization
    ])
