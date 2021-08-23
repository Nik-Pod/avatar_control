#!/usr/bin/env python3

import rospy
import selectors
import socket
from std_msgs.msg import String, Int64

pub = None
led = None


def accept(sock, mask):
    global sel
    conn, addr = sock.accept()
    print('accepted', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)


def read(conn, mask):
    global pos, led, sel
    data = conn.recv(1000)
    if data:
        data = data.decode('ascii').split()
        led_state = int(data[-1])
        positions = data[:-1]
        pos.publish(' '.join(positions))
        led.publish(led_state)
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


def talker():
    global pos, led, sel
    sel = selectors.DefaultSelector()
    pos = rospy.Publisher('positions', String, queue_size=10)
    led = rospy.Publisher('led', Int64, queue_size=10)
    rospy.init_node('tcp_server', anonymous=True)
    sock = socket.socket()
    sock.bind(('192.168.10.112', 11000))
    sock.listen(100)
    sock.setblocking(False)
    sel.register(sock, selectors.EVENT_READ, accept)
    while not rospy.is_shutdown():
        events = sel.select()
        for key, mask in events:
            callback = key.data
            callback(key.fileobj, mask)


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
