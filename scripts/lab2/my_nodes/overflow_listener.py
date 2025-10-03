#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("I heard: %s" % msg.data)

rospy.init_node('overflow_listener')
rospy.Subscriber('overflow_topic', String, callback, queue_size=10)
rospy.spin()