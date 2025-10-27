#!/usr/bin/env python3
import rospy
import math
import tf
from geometry_msgs.msg import Twist
import turtlesim.srv

if __name__ == '__main__':
    rospy.init_node('tf_turtle')

    listener = tf.TransformListener() ## to read transformations between coordiante systems

    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn) ##to spawn with set coords, rotations and a name
    spawner(4, 2, 0, 'turtle2')

    turtle_vel = rospy.Publisher('turtle2/cmd_vel', Twist, queue_size=1) ## to get turtle velocity and  publish it to cmd_vel topic

    rate = rospy.Rate(10.0)
    msg = Twist()

    while not rospy.is_shutdown():
        try:
            (trans, rot) = listener.lookupTransform('/turtle2', '/carrot', rospy.Time()) #trans - linear offset between turtles
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException): # rot - rotation 
            continue

        msg.linear.x = 0.5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
        msg.angular.z = 4 * math.atan2(trans[1], trans[0])

        turtle_vel.publish(msg)

        rate.sleep()