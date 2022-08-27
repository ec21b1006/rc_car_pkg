#!/usr/bin/env python3

import sys
import tty
import termios
import time
import rospy
#ros msgs
from std_msgs.msg import Int32


def getTerminalSettings():
    if sys.platform == 'win32':
        return None
    return termios.tcgetattr(sys.stdin)


def readKey(settings):
    if sys.platform == 'win32':
        # getwch() returns a string on Windows
        key = msvcrt.getwch()
    else:
        tty.setraw(sys.stdin.fileno())
        # sys.stdin.read() returns a string on Linux
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

rospy.init_node('rc_control',anonymous=True)

rc_front_back_pub= rospy.Publisher('/back_vel',Int32,queue_size=20)

if __name__ == '__main__':

    settings=getTerminalSettings()

    try:
        
        print("reading key strokes")

        while True:
            key=readKey(settings)

            if key== 'w':
                rc_front_back_pub.publish(1)
            elif key== 's':
                rc_front_back_pub.publish(-1)
            else:
                rc_front_back_pub.publish(0)

                
            
            
    except KeyboardInterrupt:
        print("interupted!!!")

    except Exception as e:
        print(e)
