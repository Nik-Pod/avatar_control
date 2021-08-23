#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from dxl_control.dxl_control import sync_write


def cb_positions(data):
    sync_write(dxl_id=[1, 2, 3, 4, 5, 6, 7, 8], position=list(map(int, data.data.split())), speed=[300] * 8)


def dxl_control():
    rospy.init_node('dxl_control')
    rospy.Subscriber('positions', String, cb_positions)
    rospy.spin()


if __name__ == '__main__':
    dxl_control()
