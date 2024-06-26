import json

# Importeer de subscribe module van paho.mqtt om te abonneren op MQTT topics.
from paho.mqtt import subscribe

# Definieer een callback functie die wordt aangeroepen wanneer een bericht wordt ontvangen.
def on_message(client, userdata, message):
    # Decodeer het bericht payload van bytes naar een string met UTF-8 encoding.
    payload_str = message.payload.decode("utf-8")
    # Laad de JSON string in een Python dictionary.
    data = json.loads(payload_str)

    print(f"Message received on topic {message.topic}: {data}")

# Dit blok zorgt ervoor dat de code alleen wordt uitgevoerd als dit script rechtstreeks wordt uitgevoerd.
if __name__ == "__main__":
    # Definieer het topic waarop geabonneerd wordt.
    topic = "goodgarden/par_events"
    # Roep de subscribe.callback functie aan met de on_message functie als callback om te luisteren naar berichten op het gespecificeerde topic.
    subscribe.callback(on_message, topic)