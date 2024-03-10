import paho.mqtt.client as mqtt

mqtt_broker = "localhost"
mqtt_port = 1883

# Lijst waarop je je wil subscriben
mqtt_topics = ["goodgarden/devices", "goodgarden/relative_humidity"]

# Callback functie voor wanneer de client verbindt met de broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Abonneer op alle topics in de mqtt_topics lijst
    for topic in mqtt_topics:
        client.subscribe(topic)
        print(f"Subscribed to {topic}")

# Callback functie voor wanneer een bericht is ontvangen van de server
def on_message(client, userdata, msg):
    # Decodeer de payload van bytes naar string
    message = msg.payload.decode()
    print(f"Message received on topic {msg.topic}: {message}")
    # Hier kun je code toevoegen om iets te doen met het ontvangen bericht
    # Bijvoorbeeld: de data opslaan, een actie uitvoeren, etc.

# Maak de MQTT Client aan
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Verbind met de broker
client.connect(mqtt_broker, mqtt_port, 60)

# Start loop
client.loop_forever()
