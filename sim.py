#coding:utf-8
#!/usr/bin/env python
import rospy
import numpy
from std_msgs.msg import *

def talker(jointVariable, time):
	#read the joint variable and time from csv file
	jointVariable = numpy.loadtxt(open("data/jointVariable.csv","rb"), delimiter=",",skiprows=0)
	time = numpy.loadtxt(open("data/time.csv","rb"), delimiter=",",skiprows=0)
	
	#declare the publisher of each joint
	pubJoint1 = rospy.Publisher('/ur5/joint1_position_controller/command', Float64, queue_size=10)
	pubJoint2 = rospy.Publisher('/ur5/joint2_position_controller/command', Float64, queue_size=10)
	pubJoint3 = rospy.Publisher('/ur5/joint3_position_controller/command', Float64, queue_size=10)
	pubJoint4 = rospy.Publisher('/ur5/joint4_position_controller/command', Float64, queue_size=10)
	pubJoint5 = rospy.Publisher('/ur5/joint5_position_controller/command', Float64, queue_size=10)
	pubJoint6 = rospy.Publisher('/ur5/joint6_position_controller/command', Float64, queue_size=10)
	
	#initialize a node for publishing message
	rospy.init_node('talker', anonymous=True)
	
	#set the update rate of publisher (100 refer to 100Hz)
	rate = rospy.Rate(100)
	i = 0
	while not rospy.is_shutdown():
		if i<len(time):
			#publish the joint variable to according joint
			pubJoint1.publish(jointVariable[i,0])
			pubJoint2.publish(jointVariable[i,1])
			pubJoint3.publish(jointVariable[i,2])
			pubJoint4.publish(jointVariable[i,3])
			pubJoint5.publish(jointVariable[i,4])
			pubJoint6.publish(jointVariable[i,5])
			i += 1
		else:
			break
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
