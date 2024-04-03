# Importeer de json module om met JSON data te werken.
import json

# Importeer de subscribe module van paho.mqtt om te abonneren op MQTT topics.
from paho.mqtt import subscribe

# Definieer een callback functie die wordt aangeroepen wanneer een bericht wordt ontvangen.
def on_message(client, userdata, message):
    # Decodeer het bericht payload van bytes naar een string met UTF-8 encoding.
    payload_str = message.payload.decode("utf-8")
    # Laad de JSON string in een Python dictionary.
    data = json.loads(payload_str)

    # Initialiseer variabelen om de waarden van de apparaten op te slaan.
    device_322_value = None
    device_256_value = None

    # Doorloop de "results" key in de data dictionary.
    for key in data["results"]:
        # Controleer of de "device" key overeenkomt met device 322 of 256 en sla de waarde op.
        if key["device"] == 322:
            device_322_value = key["value"]
        elif key["device"] == 256:
            device_256_value = key["value"]

    # Print de waarden van beide apparaten.
    print(f"Device 322 value: {device_322_value}")
    print(f"Device 256 value: {device_256_value}")

    # Print het volledige bericht dat ontvangen is op het abonnementstopic.
    print(f"Message received on topic {message.topic}: {data}")

# Dit blok zorgt ervoor dat de code alleen wordt uitgevoerd als dit script rechtstreeks wordt uitgevoerd.
if __name__ == "__main__":
    # Definieer het topic waarop geabonneerd wordt.
    topic = "goodgarden/par_events"
    # Roep de subscribe.callback functie aan met de on_message functie als callback om te luisteren naar berichten op het gespecificeerde topic.
    subscribe.callback(on_message, topic)
