import requests
import time
import paho.mqtt.client as mqtt
from db_connect import database_connect

mqtt_broker = "localhost"
mqtt_port = 1883
publish_interval = 300 # Secondes om een aanvraag te doen

api_endpoints = [
    {"url": "https://garden.inajar.nl/api/devices/", "topic": "goodgarden/devices"},
    {"url": "https://garden.inajar.nl/api/relative_humidity_events/", "topic": "goodgarden/relative_humidity"},
    {"url": "https://garden.inajar.nl/api/battery_voltage_events/", "topic": "goodgarden/battery_voltage"},
    {"url": "https://garden.inajar.nl/api/soil_electric_conductivity_events/", "topic": "goodgarden/soil_electric_conductivity"},
    {"url": "https://garden.inajar.nl/api/soil_relative_permittivity_events/", "topic": "goodgarden/soil_electric_permittivity"},
    {"url": "https://garden.inajar.nl/api/soil_temperature_events/", "topic": "goodgarden/soil_temperature"},
    {"url": "https://garden.inajar.nl/api/par_events/", "topic": "goodgarden/par_events"}
]

client = mqtt.Client()
client.connect(mqtt_broker, mqtt_port, 60)
client.loop_start()

def publish_to_mqtt(topic, data):
    """
    Publiceer de opgehaalde data naar een MQTT-topic.
    """
    client.publish(topic, str(data))
    print(f"Data published to MQTT topic {topic}.")

def fetch_and_publish_data():
    """
    Haal data op van alle endpoints en publiceer naar MQTT.
    """
    for endpoint in api_endpoints:
        url = endpoint["url"]
        mqtt_topic = endpoint["topic"]
        access_token = "33bb3b42452306c58ecedc3c86cfae28ba22329c"
        try:
            headers = {
                "Authorization": f"Token {access_token}"
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            print(f"Data from {url}:")
            print(data)
            # Publiceer naar MQTT voordat de data wordt geladen in de database
            publish_to_mqtt(mqtt_topic, data)
            # Hier kan je de data laden naar je database
            load_data(data)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {url}: {e}")

def load_data(data):
    """
    Implementeer de database logica hier.
    Deze functie moet mogelijk worden aangepast om te werken met verschillende datastructuren van verschillende endpoints.
    """
    print("Data processing and loading logic goes here.")

if __name__ == "__main__":
    while True:
        fetch_and_publish_data()
        print("Waiting for the next retrieval action...")
        time.sleep(publish_interval)

client.loop_stop()
