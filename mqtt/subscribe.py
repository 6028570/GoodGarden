from mqtt_client import create_client, start_loop

# Lijst waarop je je wil subscriben
mqtt_topics = [
    "goodgarden/devices", 
    "goodgarden/relative_humidity"
]

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Abonneer op alle topics in de mqtt_topics lijst
    for topic in mqtt_topics:
        client.subscribe(topic)
        print(f"Subscribed to {topic}")

def on_message(client, userdata, msg):
    # Decodeer de payload van bytes naar string
    message = msg.payload.decode()
    print(f"Message received on topic {msg.topic}: {message}")
    # Hier kun je code toevoegen om iets te doen met het ontvangen bericht

if __name__ == "__main__":
    client = create_client("subscriber1", on_connect, on_message)  # Zorg voor een unieke client ID
    start_loop(client)