#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("I heard: %s" % msg.data)

rospy.init_node('evens_listener')
rospy.Subscriber('yap_topic', String, callback, queue_size=10)
rospy.spin()