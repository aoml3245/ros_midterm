import sys
import flask
from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = AddTwoInts.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

from flask import Flask, request
from flask_cors import CORS

# Create a Flask web application
app = Flask(__name__)
CORS(app)

minimal_client = None

@app.route('/key')
def home():
    key = request.args.get('key', type = int)
    global minimal_client
    response = minimal_client.send_request(key, -1)
    minimal_client.get_logger().info(
        'Result: = %d' %(key))
    print(key)
    return str(key)

def main(args=None):
    rclpy.init()
    global minimal_client
    minimal_client = MinimalClientAsync()
    app.run()

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
