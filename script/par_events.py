import sys
import uuid

from os.path import dirname, abspath, join

root_dir = dirname(dirname(abspath(__file__)))
sys.path.append(root_dir)

from mqtt.mqtt_client import create_client, start_loop

mqtt_topic = "goodgarden/par_events"

def on_connect(client, userdata, flags, rc):
        client.subscribe(mqtt_topic)
        print(f"Subscribed to {mqtt_topic}")

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print(f"Message received on topic {msg.topic}: {message}")

if __name__ == "__main__":
    unique_client_id = f"subscriber_{uuid.uuid4()}"
    client = create_client(unique_client_id, on_connect, on_message)
    start_loop(client)