import rclpy
import math
from rclpy.node import Node
from geometry_msgs.msg import Twist
from autoware_auto_control_msgs.msg import AckermannControlCommand

WHEELBASE = 0.5

''' TODO Uplink
/vehicle/status/actuation_status
/vehicle/status/battery_charge
/vehicle/status/control_mode
/vehicle/status/gear_status
/vehicle/status/hazard_lights_status
/vehicle/status/steering_status
/vehicle/status/turn_indicators_status
/vehicle/status/velocity_status
'''

''' TODO Donwlink - To move the rover just use /cmd_vel .
/cmd_vel:
To move forward, set linear.x > 0.0
To move backward, set linear.x < 0.0
To turn, set angular.z ≠ 0.0
'''

class VehicleInterface(Node):
    def __init__(self):
        super().__init__('vehicle_interface')

        #Downlink: control speed and direction
        self.sub = self.create_subscription(
            AckermannControlCommand,
            '/control/command/control_cmd',
            self.control_cmd_callback,
            10
        )
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        #TODO: Saber l'estructura de cada msg:
        #TODO: Uplink: actuation_status 
        #TODO: Uplink: battery_charge 
        #TODO: Uplink: control_mode 
        #TODO: Uplink: gear_status 
        #TODO: Uplink: hazard_lights_status 
        #TODO: Uplink: steering_status 
        #TODO: Uplink: turn_indicators_status 
        #TODO: Uplink: velocity_status
        
    def control_cmd_callback(self, msg):
        twist = Twist()
        twist.linear.x = msg.longitudinal.speed

        # Convert steering angle to yaw rate
        steering_angle = msg.lateral.steering_tire_angle
        twist.angular.z = twist.linear.x * math.tan(steering_angle) / WHEELBASE

        self.cmd_pub.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = VehicleInterface()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
