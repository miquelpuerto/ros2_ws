import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from autoware_auto_control_msgs.msg import AckermannControlCommand

class VehicleInterface(Node):
    def __init__(self):
        super().__init__('vehicle_interface')

        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.sub = self.create_subscription(
            AckermannControlCommand,
            '/control/command/control_cmd',
            self.control_cmd_callback,
            10
        )

    def control_cmd_callback(self, msg):
        twist = Twist()
        twist.linear.x = msg.longitudinal.speed  # Forward velocity
        twist.angular.z = msg.lateral.steering_tire_angle  # Steering as yaw rate
        self.cmd_pub.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = VehicleInterface()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
