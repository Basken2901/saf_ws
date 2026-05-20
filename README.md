### How to run this project (Ubuntu Linux for ROS, Windows for CODESYS)
Make sure to be on the same network, else the data would be published to the wrong network and nothing is recieved on the server end.
1. Clone Github Repo
```
git clone {SSH Key}
```
2. Build and source the workspace
```
cd saf_ws
colcon build
source install/setup.bash
```
3. Run the TCP Server host using ROS on Ubuntu Linux
```
ros2 run saf_tcpserver server_node
ros2 run saf_tcpserver logger_node
```
4. Run the PLC project on Windows
