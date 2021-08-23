#!/usr/bin/env python3
import rospy
import RPi.GPIO as GPIO
from std_msgs.msg import Int64

LED_GPIO = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_GPIO, GPIO.OUT)


def cb_led_state(data):
    led_state = data.data
    if led_state == 1:
        GPIO.output(LED_GPIO, GPIO.HIGH)
    elif led_state == 0:
        GPIO.output(LED_GPIO, GPIO.LOW)


def led_control():
    rospy.init_node('led_control')
    rospy.Subscriber('led', Int64, cb_led_state)
    rospy.spin()


if __name__ == "__main__":
    led_control()
