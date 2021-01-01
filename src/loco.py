#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import time


#################################### DO N0T TOUCH THE FOLLOWING LINES #############################################
                                                                                                                   
rospy.init_node('vel_Publisher')																				   
b_pub = rospy.Publisher('/open_base/back_joint_velocity_controller/command', Float64, latch=True, queue_size=1)    
l_pub = rospy.Publisher('/open_base/left_joint_velocity_controller/command', Float64, latch=True, queue_size=1)    
r_pub = rospy.Publisher('/open_base/right_joint_velocity_controller/command', Float64, latch=True, queue_size=1)   
																							                       
def motor_left(l_dir, speed):                                                                                      
	vel = Float64()                                                                                                
	if speed > 30:                                                                                                 
		l_vel = 30                                                                                                 
	else:             																							   
		l_vel = speed																							   
	if l_dir == 'cw':																							   
		vel = l_vel 																							   
	elif l_dir == 'ccw':																						   
		vel = -1 * l_vel 																						   
	elif l_dir == 'stop':																						   
		vel = 0																									   
	l_pub.publish(vel)																							   
																												   
def motor_right(r_dir, speed):																					   
	vel = Float64()																								   
	if speed > 30:                                                                                                 
		r_vel = 30                                                                                                 
	else:                                                                                                          
		r_vel = speed                                                                                              
	if r_dir == 'cw':                                                                                              
		vel = r_vel                                                                                                
	elif r_dir == 'ccw':                                                                                           
		vel = -1 * r_vel                                                                                           
		vel = 0                                                                                                   
	r_pub.publish(vel)                                                                                             
                                                                                                                   
def motor_back(b_dir, speed):                                                                                      
	vel = Float64()                                                                                                
	if speed > 30:                                                                                                 
		b_vel = 30                                                                                                 
	else:                                                                                                          
		b_vel = speed                                                                                              
	if b_dir == 'cw':                                                                                              
		vel = b_vel                                                                                                
	elif b_dir == 'ccw':                                                                                           
		vel = -1 * b_vel                                                                                           
	elif b_dir == 'stop':                                                                                          
		vel = 0                                                                                                    
	b_pub.publish(vel)                                                                                             
                                                                                                                   
####################################################################################################################


def main():

	while not rospy.is_shutdown():

		motor_left('cw', 10)
		motor_right('cw', 10)
		motor_back('ccw', 20)



if __name__ == "__main__":
	main()