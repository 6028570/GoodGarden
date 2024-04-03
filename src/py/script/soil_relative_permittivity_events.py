# Importeer de json module om te werken met JSON data.
import json

# Importeer de subscribe functie van paho.mqtt om te abonneren op MQTT berichten.
from paho.mqtt import subscribe

# Definieer een functie die wordt aangeroepen wanneer een bericht wordt ontvangen op het gespecificeerde MQTT topic.
def on_message(client, userdata, message):
    # Decodeer de berichtpayload van bytes naar een UTF-8 string.
    payload_str = message.payload.decode("utf-8")
    # Laad de JSON string in een Python dictionary om gemakkelijk met de data te kunnen werken.
    data = json.loads(payload_str)

    # Print een bericht uit met de topicnaam en de ontvangen data.
    print(f"Message received on topic {message.topic}: {data}")

# Het hoofdscript dat wordt uitgevoerd wanneer dit bestand direct wordt gerund.
if __name__ == "__main__":
    # Specificeer het MQTT-topic waarop we willen abonneren. In dit geval luisteren we naar data over de relatieve permittiviteit van de bodem.
    topic = "goodgarden/soil_relative_permittivity"
    # Roep de subscribe.callback functie aan met de on_message functie als argument. Dit zorgt ervoor dat we voortdurend luisteren naar berichten op het gegeven topic.
    subscribe.callback(on_message, topic)
