# Importeer benodigde modules voor het uitvoeren van HTTP-verzoeken, tijdbeheer, en JSON-operaties.
import requests
import time
import json

# Importeer MQTT-client functies van een aangepaste module.
from mqtt_client import create_client, start_loop  

# Stel het interval in seconden in voor het periodiek ophalen en publiceren van data.
publish_interval = 30  # MOET ~300 ZIJN voor productiegebruik.

# Definieer API-eindpunten en de corresponderende MQTT topics.
api_endpoints = [
    {"url": "https://garden.inajar.nl/api/devices/", "topic": "goodgarden/devices"},
    # Voeg meer API-eindpunten en topics toe zoals vereist.
]

def on_connect(client, userdata, flags, rc):
    """
    Callback functie voor het afhandelen van de connectie-event met de MQTT broker.
    
    Parameters:
        client: De MQTT-client instantie.
        userdata: De private user-specifieke data zoals ingesteld in Client() of user_data_set().
        flags: Reactie vlaggen van de broker.
        rc: De connectie resultaat code.
    """
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    """
    Callback functie voor het afhandelen van inkomende berichten voor geabonneerde topics.
    
    Parameters:
        client: De MQTT-client instantie.
        userdata: De private user-specifieke data.
        msg: Het bericht instantie.
    """
    print(f"Message: {msg.topic} {str(msg.payload)}")

# Initialiseer de MQTT-client met een unieke client ID en callback functies.
client = create_client("publisher1", on_connect, on_message)

def publish_to_mqtt(topic, data):
    """
    Publiceert data naar een MQTT topic.
    
    Parameters:
        topic (str): Het MQTT topic waarop de data wordt gepubliceerd.
        data (dict): De data die gepubliceerd moet worden, geconverteerd naar JSON formaat.
    """
    json_data = json.dumps(data)  # Serialiseer de data naar een JSON-string.
    client.publish(topic, json_data)
    print(f"\033[92mData published to MQTT topic {topic}.\033[0m")

def fetch_and_publish_data():
    """
    Haalt data op van API-eindpunten en publiceert deze naar MQTT.
    """
    for endpoint in api_endpoints:
        url = endpoint["url"]
        mqtt_topic = endpoint["topic"]
        access_token = "33bb3b42452306c58ecedc3c86cfae28ba22329c"  # Voorbeeld token.

        try:
            headers = {"Authorization": f"Token {access_token}"}
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Verifieert respons status.
            data = response.json()
            print(f"Data from {url}: {data}")
            publish_to_mqtt(mqtt_topic, data)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {url}: {e}")

if __name__ == "__main__":
    client.loop_start()  # Start de niet-blokkerende MQTT-client loop.
    while True:
        fetch_and_publish_data()  # Haal data op en publiceer.
        print(f"\033[91mWachten, wachten en nog eens wachten... {publish_interval} secondes!\033[0m\n")
        time.sleep(publish_interval)  # Wacht voor het ingestelde interval.

        client.loop_stop()
