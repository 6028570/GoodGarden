import json

# Van de paho.mqtt bibliotheek wordt de subscribe module geïmporteerd.
# Deze module stelt ons in staat om ons te abonneren op MQTT-topics en berichten te ontvangen.
from paho.mqtt import subscribe

# Definitie van de functie on_message die wordt aangeroepen wanneer een bericht wordt ontvangen.
def on_message(client, userdata, message):
    # De payload van het bericht, dat in bytes is, wordt gedecodeerd naar een UTF-8 string.
    payload_str = message.payload.decode("utf-8")
    # De gedecodeerde string, die in JSON-formaat is, wordt omgezet naar een Python dictionary.
    data = json.loads(payload_str)

    # Een bericht wordt geprint naar de console met de informatie over het ontvangen bericht.
    print(f"Message received on topic {message.topic}: {data}")

# Dit blok zorgt ervoor dat de volgende code alleen uitgevoerd wordt als dit script direct wordt uitgevoerd.
if __name__ == "__main__":
    # Het MQTT-topic waarop het script zich abonneert, gerelateerd aan de elektrische geleidbaarheid van de bodem.
    topic = "goodgarden/soil_electric_conductivity"
    # De subscribe.callback functie wordt aangeroepen met de on_message functie als callback.
    # Dit start het proces van luisteren naar berichten op het gespecificeerde topic.
    subscribe.callback(on_message, topic)
