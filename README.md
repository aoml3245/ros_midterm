0. you have to setup the ros foxy environment, nodejs, npm environment and python
   
	pip install flask_cors flask
	
2. open three terminal (A, B, C)
   
4. build the our package(in ros_ws_folder)

	colcon build

2. source the ros setup(in ros_ws folder)
   
	[terminal A, B] source /opt/ros/foxy/setup.bash

	[terminal A, B] source {git_folder}/ros_ws/install/setup.bash

4. run the ros_client and ros_server
   
	[terminal A] ros2 run flask_ros server

	[terminal B] ros2 run flask_ros client

6. connect to pcb board( you need to unregister wifi, and the board must be ap mode with 192.168.0.1)
   
8. run the node web(in web folder)
   
	[terminal C] npm i

	[terminal C] npm start

10. open web and enjoy
