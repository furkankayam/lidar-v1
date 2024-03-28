#   python3.6

import random
from paho.mqtt import client as mqtt_client
import json

#   Code for MQTT Connection
broker = '192.168.1.145'
port = 1883
topic = "py"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'


#   Function to connect on mqtt
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

#   function to subscribe from mqtt
def subscribeFunc(client: mqtt_client):
    def on_messageFunc(client, userdata, msg):
        #print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        print(msg.payload.decode())

    client.subscribe(topic)
    client.on_message = on_messageFunc


def run():
    client = connect_mqtt()
    subscribeFunc(client)
    client.loop_forever()


if __name__ == '__main__':
    run()