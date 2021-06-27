# RMA_PROJETC_01
In this repository, there are files to be used in conjunction with Turtlebot3. With these files you will be able to run Turtlebot3 inside a maze and go from the starting point to another point on the map automatically.  This repository was created to store the solution of research work 01 of the discipline Mobile autonomous robots. Provided by the Graduate Program in Computer Science at UFSCar Sorocaba.

Group: 
  Nome: Ariel Campos 
  RA: 761273
  email: arielcampos@estudante.ufscar.br
  
  Nome: Públio Elon Corrêa da Silva
  RA: 18811345
  email: publio@estudante.ufscar.br

# Pre-Requisites
- Ubuntu 20.04.2.0 LTS (Focal Fossa)
- ROS nsimulator [here] https://www.laris.ufscar.br/pt-br/pessoal/simulator-mrs

# Install and configured turtlebot3
If you prefer to install the turtlebot3 environment from scratch follow the steps below. If you want to download the configured zipped folder, follow from step 2.

## 1. Install the dependencies step to step

    If 
- $ source /opt/ros/noetic/setup.bash
- $ sudo apt-get install ros-noetic-turtlebot3-msgs
- $ sudo apt-get install ros-noetic-turtlebot3

## 1.1 Building the packages

- $ cd workspace/src
-  git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3
- $ git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations
- $ git clone https://github.com/fazildgr8/ros_autonomous_slam.git
- $ cd ..
- $ catkin_make
- $ source /devel/setup.bash

The Navigation stack can also be downloaded as source files to your workspace and built.

- $ sudo apt-get install ros-noetic-navigation
- $ cd workspace/src
- $ git clone -b noetic-devel https://github.com/ros-planning/navigation
- $ cd ..
- $ catkin_make
- $ source /devel/setup.bash

## 1.2 Copy files in folders corrects
### In folder ros_autonomous_slam
- Copy the file turtlebot3_maze.launch in ~/workspace/src/ros_autonomous_slam/launch
- Copy the files maze.pgm and maze.yaml in ~/workspace/src/ros_autonomous_slam/maps
- Copy the files maze.py in ~/workspace/src/ros_autonomous_slam/nodes
- Copy the files testWorld.world in ~/workspace/src/ros_autonomous_slam/worlds

### In folder turtlebot3_simulations
- Copy the folder maze in ~/workspace/src/turtlebot3_simulations/turtlebot3_gazebo/models
- Copy the files testWorld.world in ~/workspace/src/turtlebot3_simulations/turtlebot3_gazebo/worlds

# 2. Folder already configured
- Copy internal folder of turtlebot3_maze_configured in ~/workspace/src

###  Compile the environment with catkin
- $ cd ~/workspace/src/
- $ catkin build
- $ source /devel/setup.bash

# Run launch maze
Execute this commands in terminal:
- Close all terminal open
- Open new terminal
- $ source ~/.bashrc
- $ cd /workspace
- $ export TURTLEBOT3_MODEL=waffle_pi
- $roslaunch ros_autonomous_slam turtlebot3_maze.launch