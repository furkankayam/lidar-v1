# Import package
import paho.mqtt.client as mqtt

# Define Variables
MQTT_HOST = "192.168.1.145"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "py"
MQTT_MSG = '{\n"message": "hello MQTT"\n}'


# Define on_publish event function
def on_publish(client, userdata, mid):
	print("Message Published...")

# Initiate MQTT Client
mqttc = mqtt.Client()

# Register publish callback function
mqttc.on_publish = on_publish

# Connect with MQTT Broker
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)		

# Publish message to MQTT Broker	
mqttc.publish(MQTT_TOPIC,MQTT_MSG)

# Disconnect from MQTT_Broker
mqttc.disconnect()