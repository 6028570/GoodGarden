import json

from paho.mqtt import subscribe

def on_message(client, userdata, message):
    payload_str = message.payload.decode("utf-8")
    data = json.loads(payload_str)

    device_256 = 0
    device_322 = 0

    for key in data["results"]:
        if int(key["id"]) == 256:
            device_256 = int(key["id"])
            print(f"{device_256}")

        elif int(key["id"]) == 322:
            device_322 = int(key["id"])
            print(f"{device_322}")

    print(f"Message received on topic {message.topic}: {data}")

if __name__ == "__main__":
    topic = "goodgarden/devices"
    subscribe.callback(on_message, topic)