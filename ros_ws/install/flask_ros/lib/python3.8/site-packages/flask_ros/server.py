from example_interfaces.srv import AddTwoInts

import rclpy
from rclpy.node import Node
import requests

class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)

    def add_two_ints_callback(self, request, response):
        response.sum = request.a
        self.get_logger().info('Incoming request\nkey: %d' % (request.a))
        requests.get("http://192.168.0.1/command?commandText=G92%20X0%20Y0")
        if request.a == 0:
            requests.get("http://192.168.0.1/command?commandText=G92%20X0%20Y0")
            pass
        if request.a == 1:
            requests.get("http://192.168.0.1/command?commandText=G1%20X10%20Y10")
            pass
        if request.a == 2:
            requests.get("http://192.168.0.1/command?commandText=G1%20X-10%20Y-10")
            pass
        return response


def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
