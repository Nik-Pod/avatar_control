import rospy
from std_msgs.msg import Int64
import paho.mqtt.client as mqtt

mqtt_topic = "distAmp"
mqtt_broker_ip = "192.168.10.112"

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    client.subscribe(mqtt_topic)


def on_message(client, userdata, msg):
    data = str(msg.payload)
    light = float(data.split()[0])
    if light < 10.0:


def grab():
    global grab_state
    rospy.init_node()
