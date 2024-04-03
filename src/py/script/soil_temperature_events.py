# Importeer de json module om te werken met JSON-geformatteerde data.
import json

# Importeer de subscribe functie van de paho.mqtt bibliotheek voor MQTT communicatie.
from paho.mqtt import subscribe

# Definieer de on_message functie die wordt uitgevoerd wanneer een bericht wordt ontvangen.
def on_message(client, userdata, message):
    # Decodeer de payload van het bericht van bytes naar een UTF-8 gecodeerde string.
    payload_str = message.payload.decode("utf-8")
    # Converteer de JSON string naar een Python dictionary om het gemakkelijker te verwerken.
    data = json.loads(payload_str)

    # Print de ontvangen data samen met het topic waarop het bericht is ontvangen.
    print(f"Message received on topic {message.topic}: {data}")

# Het hoofdgedeelte van het script dat wordt uitgevoerd als het script direct wordt aangeroepen.
if __name__ == "__main__":
    # Definieer het MQTT-topic waarop we willen abonneren, in dit geval bodemtemperatuur.
    topic = "goodgarden/soil_temperature"
    # Start het abonneren op het opgegeven topic met de on_message functie als de callback.
    subscribe.callback(on_message, topic)
