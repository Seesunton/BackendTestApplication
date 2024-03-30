"""
เขียนโปรแกรมอะไรก็ได้ที่อยาก present Python's skill set เจ๋ง ๆ ของตัวเอง
ข้อนี้ไม่ต้องทำก็ได้ ไม่มีผลลบกับการให้คะแนน แต่ถ้าทำมาเเล้วเจ๋งจริง ก็จะพิจารณาเป็นพิเศษ

"""
import paho.mqtt.client as mqtt

# MQTT broker settings
broker_address = "192.168.100.29"
broker_port = 1883
username = "Hello"
password = "Swift Dynamics"
topic = "test"

# Callback functions
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_publish(client, userdata, mid):
    print("Message published")


client = mqtt.Client()


client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish


client.username_pw_set(username, password)

# Connect to broker
client.connect(broker_address, broker_port)


client.loop_start()

# Publish a test message
client.publish(topic, "Hello MQTT")


try:
    while True:
        pass
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
    print("Disconnected and program terminated.")
