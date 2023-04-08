#!/usr/bin/env python3
import rospy


import tf2_ros

from nav_msgs.msg import Odometry
import geometry_msgs.msg

import config



def handle_body_pose(msg):
    global body_offset_x, body_offset_y, body_offset_z
    body_offset_x = msg.pose.position.x
    body_offset_y = msg.pose.position.y
    body_offset_z = msg.pose.position.z


def handle_odom_pose(msg):
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "map"
    t.child_frame_id = "odom_map"


    t.transform.translation.x = body_offset_x - msg.pose.pose.position.x - config.OFFSET_X
    t.transform.translation.y = body_offset_y - msg.pose.pose.position.y - config.OFFSET_Y
    t.transform.translation.z = body_offset_z - msg.pose.pose.position.z - config.OFFSET_Z

    t.transform.rotation.x = 0
    t.transform.rotation.y = 0
    t.transform.rotation.z = 0
    t.transform.rotation.w = 1
    br.sendTransform(t)

if __name__ == '__main__':
    rospy.init_node('tf2_odom_broadcaster')

    rospy.Subscriber('/mavros/local_position/pose', geometry_msgs.msg.PoseStamped, handle_body_pose)
    rospy.Subscriber('/camera/odom/sample', Odometry, handle_odom_pose)
    rospy.spin()