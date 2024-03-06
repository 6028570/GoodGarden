import os
import time
import requests
import paho.mqtt.client as mqtt
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")
MQTT_HOST = os.getenv("MQTT_HOST")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))

def get_data_from_api(request):
    links = {
        'battery': '/battery_voltage_events/',
        'devices': '/devices/',
        'parEvents': '/par_events/',
        'humidity': '/relative_humidity_events/',
        'soilConductifity': '/soil_electric_conductivity_events/',
        'soilPermittivity' : '/soil_relative_permittivity_events/',
        'soilTemperature': '/soil_temperature_events/'
    }
    headers = {
        'accept': 'application/json',
        'Authorization': f'Token {os.getenv("API_TOKEN")}'
    }
    url = API_URL + links[request]
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:",errh)
        return None
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
        return None
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
        return None
    except requests.exceptions.RequestException as err:
        print ("Something went wrong",err)
        return None

    data = response.json()
    return data['results']

def publish_to_mqtt(topic, message):
    client = mqtt.Client()
    client.connect(MQTT_HOST, MQTT_PORT, 60)
    try:
        client.publish(topic, message)
    except mqtt.MQTTException as e:
        print(f"Failed to publish message: {e}")
    finally:
        client.disconnect()

def process_results(link, results):
    for result in results:
        if 'timestamp' in result and 'gateway_receive_time' in result and 'device' in result and 'value' in result:
            message = f"Timestamp: {result['timestamp']}, Gateway Receive Time: {result['gateway_receive_time']}, Device: {result['device']}, Value: {result['value']}"
            print(message)
            publish_to_mqtt(link, message)

def main():
    links = ['battery', 'devices', 'parEvents', 'humidity', 'soilConductifity', 'soilPermittivity', 'soilTemperature']
    while True:
        for link in links:
            results = get_data_from_api(link)
            if results is not None:
                process_results(link, results)
        time.sleep(5)

if __name__ == "__main__":
    main()