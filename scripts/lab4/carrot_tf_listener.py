#!/usr/bin/env python3
import rospy
import math
import tf

if __name__ == '__main__':
    rospy.init_node('tf_carrot')

    listener = tf.TransformListener()
    rate = rospy.Rate(10.0)
    
    #parameteres
    radius = 1.44 
    angular_speed = 0.84 
    
    starting_time = rospy.Time.now()
    
    while not rospy.is_shutdown():
        try:
            cur_time = rospy.Time.now()
            elapsed = (cur_time - starting_time).to_sec() ## to get time for carrot to move around turtle1 in time
            
            carrot_x = radius * math.cos(angular_speed * elapsed) ## get x coord based from turtle1
            carrot_y = radius * math.sin(angular_speed * elapsed) ## get y coord based from turtle1
            
            broadcaster = tf.TransformBroadcaster()
            broadcaster.sendTransform(
                (carrot_x, carrot_y, 0),
                tf.transformations.quaternion_from_euler(0, 0, 0),
                rospy.Time.now(),
                "carrot",  # child
                "turtle1"  # parent
            )
 
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        rate.sleep()