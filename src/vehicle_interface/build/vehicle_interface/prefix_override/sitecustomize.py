import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/miquel/ros2_ws/src/vehicle_interface/install/vehicle_interface'
