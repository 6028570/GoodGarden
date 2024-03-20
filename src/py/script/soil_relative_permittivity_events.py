import json

from paho.mqtt import subscribe

def on_message(client, userdata, message):
    payload_str = message.payload.decode("utf-8")
    data = json.loads(payload_str)

    print(f"Message received on topic {message.topic}: {data}")

if __name__ == "__main__":
    topic = "goodgarden/soil_relative_permittivity"
    subscribe.callback(on_message, topic)