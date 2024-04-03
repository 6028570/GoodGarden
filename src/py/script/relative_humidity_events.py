# Importeer de json module voor het werken met JSON data.
import json

# Importeer de subscribe functie uit de paho.mqtt module voor MQTT-communicatie.
from paho.mqtt import subscribe

# Definieer een callback functie die wordt aangeroepen wanneer een bericht wordt ontvangen.
def on_message(client, userdata, message):
    # Decodeer de berichtpayload van bytes naar een UTF-8 gecodeerde string.
    payload_str = message.payload.decode("utf-8")
    # Converteer de JSON string naar een Python dictionary.
    data = json.loads(payload_str)

    # Print een bericht uit met de ontvangen data en het topic waarop het bericht is ontvangen.
    print(f"Message received on topic {message.topic}: {data}")

# Het hoofdgedeelte van het script wordt alleen uitgevoerd als dit script als hoofdscript wordt gedraaid.
if __name__ == "__main__":
    # Specificeer het MQTT-topic waarop geabonneerd moet worden.
    topic = "goodgarden/relative_humidity"
    # Abonneer op het opgegeven topic en roep de on_message functie aan als callback voor ontvangen berichten.
    subscribe.callback(on_message, topic)
