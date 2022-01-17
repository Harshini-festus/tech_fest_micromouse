#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
# from rospy.names import valid_name_validator_resolved
from std_msgs.msg import Float64
from math import *
rospy.init_node('move_diffdrive') # defining the ros node - publish_node
left_wheel_veloity=rospy.Publisher("/base_to_second_joint_position_controller/command",Float64,queue_size=1)
right_wheel_velocity=rospy.Publisher("/base_to_first_joint_position_controller/command",Float64,queue_size=1)
# chasis_velocity=rospy.Publisher("/cmd_vel",Twist,queue_size=1)
rate =rospy.Rate(100) # frequency at which publishing
# move=Twist()
# move.linear.x=10
# move.angular.z=0
v_l=0
v_r=0
base_width=0.08
x=0
w=0
# velocity_l=move.linear.x+omega*l/2
# velocity_r=-(move.linear.x-omega*l/2)
def callback(msg):
	global x, w
	x=msg.linear.x
	w=msg.angular.z
	w*=10
while not rospy.is_shutdown():
	# input_x=input("linear_x")
	# input_z=input("angular_z")
	# chasis_velocity.publish(move)
	pub = rospy.Subscriber('/cmd_vel', Twist,callback)
	v_r=x+base_width*w/2
	v_l=x-base_width*w/2
	left_wheel_veloity.publish(v_l)
	right_wheel_velocity.publish(v_r)
	rate.sleep()