import sys
import uuid

from os.path import dirname, abspath, join

# Voeg het pad naar de 'root' directory toe aan sys.path
root_dir = dirname(dirname(abspath(__file__)))
sys.path.append(root_dir)

from mqtt.mqtt_client import create_client, start_loop

# Lijst waarop je je wil subscriben
mqtt_topic = "goodgarden/devices"

def on_connect(client, userdata, flags, rc):
        client.subscribe(mqtt_topic)
        print(f"Subscribed to {mqtt_topic}")

def on_message(client, userdata, msg):
    # Decodeer de payload van bytes naar string
    message = msg.payload.decode()
    print(f"Message received on topic {msg.topic}: {message}")
    # Hier kun je code toevoegen om iets te doen met het ontvangen bericht

if __name__ == "__main__":
    unique_client_id = f"subscriber_{uuid.uuid4()}"  # Zorg voor een unieke client ID, zodat meerdere subscribers kunnen runnen
    client = create_client(unique_client_id, on_connect, on_message)
    start_loop(client)