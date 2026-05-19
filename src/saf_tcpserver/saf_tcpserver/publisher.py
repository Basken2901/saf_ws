import socket
import threading

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class PLCServer(Node):

    def __init__(self):
        super().__init__('plc_server')

        # ROS publisher (like your example)
        self.publisher_ = self.create_publisher(String, 'plc_data', 10)

        # TCP setup (PLC connection)
        self.host = "0.0.0.0"
        self.port = 9999

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)

        self.get_logger().info(f"Listening on {self.host}:{self.port}")

        # Start TCP thread (important so ROS doesn't block)
        self.thread = threading.Thread(target=self.accept_clients, daemon=True)
        self.thread.start()

    def accept_clients(self):
        while True:
            client, addr = self.server.accept()
            self.get_logger().info(f"PLC connected: {addr}")

            threading.Thread(
                target=self.handle_client,
                args=(client,),
                daemon=True
            ).start()

    def handle_client(self, client):

        while True:
            data = client.recv(1024)

            if not data:
                break

            msg_text = data.decode()

            # Create ROS message (like your timer example)
            msg = String()
            msg.data = msg_text

            # Publish to ROS topic
            self.publisher_.publish(msg)

            # Log it
            self.get_logger().info(f"PLC: {msg_text}")

            # Optional ACK to PLC
            client.send(b"ACK")

        client.close()


def main(args=None):
    rclpy.init(args=args)

    node = PLCServer()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()