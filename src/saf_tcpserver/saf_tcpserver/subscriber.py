import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class PLCLogger(Node):

    def __init__(self):
        super().__init__('plc_logger')

        self.subscription = self.create_subscription(
            String,
            'plc_data',
            self.listener_callback,
            10
        )

        self.subscription  # keep reference

    def listener_callback(self, msg):
        self.get_logger().info(f'LOG: {msg.data}')


def main(args=None):
    rclpy.init(args=args)

    node = PLCLogger()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()