import rclpy
from rclpy.node import Node
from std_msgs.msg import String

import csv
import os
from datetime import datetime


class PLCLogger(Node):

    def __init__(self):
        super().__init__('plc_logger')

        # Subscribe to PLC topic
        self.subscription = self.create_subscription(
            String,
            'plc_data',
            self.listener_callback,
            10
        )

        # CSV file path (HOME directory)
        self.file_path = os.path.expanduser("~/plc_log.csv")

        # Check if file exists (to write header only once)
        file_exists = os.path.isfile(self.file_path)

        # Open file in append mode
        self.file = open(self.file_path, mode='a', newline='')
        self.writer = csv.writer(self.file)

        # Write header if new file
        if not file_exists:
            self.writer.writerow(["timestamp", "data"])

        self.get_logger().info(f"Logging to: {self.file_path}")

    def listener_callback(self, msg):

        # Timestamp
        timestamp = datetime.now().isoformat()

        # Write row to CSV
        self.writer.writerow([timestamp, msg.data])

        # Force write to disk immediately
        self.file.flush()

        # Also print to terminal
        self.get_logger().info(f'LOG: {msg.data}')

    def destroy_node(self):
        # Close file properly when ROS shuts down
        self.file.close()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)

    node = PLCLogger()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()