import requests
import time
import json

from mqtt_client import create_client, start_loop  

publish_interval = 30  # Secondes om een aanvraag te doen - MOET ~300 ZIJN!!!!!!!!!

api_endpoints = [
    {"url": "https://garden.inajar.nl/api/devices/", "topic": "goodgarden/devices"},
    {"url": "https://garden.inajar.nl/api/relative_humidity_events/", "topic": "goodgarden/relative_humidity"},
    {"url": "https://garden.inajar.nl/api/battery_voltage_events/", "topic": "goodgarden/battery_voltage"},
    {"url": "https://garden.inajar.nl/api/soil_electric_conductivity_events/", "topic": "goodgarden/soil_electric_conductivity"},
    {"url": "https://garden.inajar.nl/api/soil_relative_permittivity_events/", "topic": "goodgarden/soil_relative_permittivity"},
    {"url": "https://garden.inajar.nl/api/soil_temperature_events/", "topic": "goodgarden/soil_temperature"},
    {"url": "https://garden.inajar.nl/api/par_events/", "topic": "goodgarden/par_events"}
]

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    print(f"Message: {msg.topic} {str(msg.payload)}")

client = create_client("publisher1", on_connect, on_message)  # Gebruik een unieke client ID

def publish_to_mqtt(topic, data):

    json_data = json.dumps(data)  # Serialiseer de data naar een JSON-string
    client.publish(topic, json_data)
    print(f"Data published to MQTT topic {topic}.")

def fetch_and_publish_data():

    for endpoint in api_endpoints:
        url = endpoint["url"]
        mqtt_topic = endpoint["topic"]
        access_token = "33bb3b42452306c58ecedc3c86cfae28ba22329c"

        try:
            headers = {"Authorization": f"Token {access_token}"}
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Zorgt ervoor dat HTTPError wordt opgeworpen voor slechte responses
            data = response.json()
            print(f"Data from {url}: {data}")
            publish_to_mqtt(mqtt_topic, data)
            # load_data(data)  # Zorg ervoor dat deze functie elders gedefinieerd is
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {url}: {e}")

if __name__ == "__main__":
    client.loop_start()  # Start de niet-blokkerende loop
    while True:
        fetch_and_publish_data()
        print("Wachten, wachten en nog eens wachten...")
        time.sleep(publish_interval)
    client.loop_stop()
