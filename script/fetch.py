import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = str(msg.payload.decode("utf-8"))
    print(f"Message received on topic {topic}: {payload}")
    if topic == "goodgarden/temperature":
        # Verwerk temperatuurdata
    # elif topic == "goodgarden/humidity":
        print(f"Message received on topic {topic}: {payload}")
        # Verwerk vochtigheidsdata
    # Voeg meer condities toe voor andere subtopics