#!/usr/bin/env python3
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def send_goal_route(position_x, position_y, orientation_z):
    route = MoveBaseGoal()
    route.target_pose.header.frame_id = 'map' 
    route.target_pose.pose.position.x = position_x
    route.target_pose.pose.position.y = position_y
    route.target_pose.pose.orientation.z = orientation_z
    return route

def main():
    rospy.init_node('send_client_goal')
    action = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
    action.wait_for_server()

    # Define values
    position_x = -6.10
    position_y = 17.20
    orientation_z = 0.8
    
    # Dispatch Send goal
    action.send_goal(send_goal_route(position_x, position_y, orientation_z))


if __name__ == '__main__':
    main()
