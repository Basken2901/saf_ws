### How to run this project (Ubuntu Linux for ROS, Windows for CODESYS)
2 PC's are needed. One for running the ROS2 server, which is going to recieve data sent from the PLC (Ubuntu Linux). The other is for running the PLC project on CODESYS (Windows). Make sure to be on the same network, else the data would be published to the wrong network and nothing is recieved on the server end.
1. Clone Github Repo (Ubuntu Linux)
```
git clone {SSH Key}
```
2. Build and source the workspace (Ubuntu Linux)
```
cd saf_ws
colcon build
source install/setup.bash
```
3. Run the TCP Server host using ROS (Ubuntu Linux)
```
ros2 run saf_tcpserver server_node
ros2 run saf_tcpserver logger_node
```
4. Run the PLC project (Windows)

Open CODESYS and load the "SAF Workshop.project"

5. Change the IPV4 address in the project (ONLY Windows)

Change the current IPV4 address in the CODESYS project file, to the IPV4 address of the server pc (Ubuntu Linux).
This is where it is important to be connected to the same wifi!

6. Connect to the PLC and run (Windows)
