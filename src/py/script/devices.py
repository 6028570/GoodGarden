import json

from paho.mqtt import subscribe

def on_message(client, userdata, message):
    payload_str = message.payload.decode("utf-8")
    data = json.loads(payload_str)

    device_256 = None
    last_seen = None
    last_battery_voltage = None

    device_322 = None
    last_seen = None
    last_battery_voltage = None

    for key in data["results"]:
        if int(key["id"]) == 256:
            device_256 = int(key["id"])
            last_seen = int(key["last_seen"])
            last_battery_voltage = float(key["last_battery_voltage"])
            # print(f"{device_256}")
            print(f"Het device {device_256} is voor het laatst geien op: {last_seen} met de voltage als {last_battery_voltage}")

        elif int(key["id"]) == 322:
            device_322 = int(key["id"])
            last_seen = int(key["last_seen"])
            last_battery_voltage = float(key["last_battery_voltage"])
            # print(f"{device_256}")
            print(f"Het device {device_322} is voor het laatst gezien op: {last_seen} met de voltage als {last_battery_voltage}")

    print(f"\033[92mMessage received on topic\033[0m {message.topic}: {data}")

if __name__ == "__main__":
    topic = "goodgarden/devices"
    subscribe.callback(on_message, topic)