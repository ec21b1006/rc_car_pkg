#!/usr/bin/env python3

import rospy

from std_msgs.msg import Int32


rospy.init_node('temp',anonymous=True)

def temp_callback(val):
    print(val)

if __name__ == '__main__':

    rospy.Subscriber("/cmd_vel",Int32, temp_callback)
    print("f")
    rospy.spin()