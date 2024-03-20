import json

from paho.mqtt import subscribe

def on_message(client, userdata, message):
    payload_str = message.payload.decode("utf-8")
    data = json.loads(payload_str)

    device_322_value = None
    device_256_value = None

    for key in data["results"]:
        if key["device"] == 322:
            device_322_value = key["value"]
        elif key["device"] == 256:
            device_256_value = key["value"]

    print(f"Device 322 value: {device_322_value}")
    print(f"Device 256 value: {device_256_value}")

    print(f"Message received on topic {message.topic}: {data}")

if __name__ == "__main__":
    topic = "goodgarden/par_events"
    subscribe.callback(on_message, topic)