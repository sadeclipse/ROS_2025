#!/usr/bin/env python3

import rospy
rospy.init_node('params_study')
distro = rospy.get_param('/rosdistro')

rospy.set_param('~ros_priv_param', 'Hi, I am private =)')
rospy.set_param('ros_loc_param', 'Hi, I am local =)')
rospy.set_param('/ros_glob_param', 'Hi, I am global =)')