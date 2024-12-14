import rclpy
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args)  # Initialize rclpy
    node = Node("py_test") 
    # Use the node's logger to log a message
    node.get_logger().info("Hello ROS2")
    rclpy.spin(node)  # Keep the node alive to handle callbacks
    # Shutdown and cleanup
    node.destroy_node() 
    rclpy.shutdown()

if __name__ == "__main__":
    main()

