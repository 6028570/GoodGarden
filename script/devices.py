# import requests
# import time

# from db_connect import database_connect

# def fetch_and_display_all(url, access_token):
#     # for _ in range(repeat_count):
#     try:
#          headers = {
#              "Authorization": f"Token {access_token}"
#          }
#          response = requests.get(url, headers=headers)
#          response.raise_for_status()
#          data = response.json()
#          print(f"Data from {url}:")
#          print(data)
#          load_data(data)
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching data from {url}: {e}")
#         print("Waiting for the next retrieval action...")
#      # time.sleep(300)  # Time here is in seconds.
#     time.sleep(1)  # Time here is in seconds.

# def load_data(data):
#     mydb = database_connect()
#     if mydb.is_connected():
#         mycursor = mydb.cursor()

#         # Here you need to adjust the correct column names and data formats based on the API response
#         insert_query = """
#         INSERT INTO goodgarden.devices (serial_number, name, label, last_seen, last_battery_voltage)
#         VALUES (%s, %s, %s, %s, %s )
#         """
#         for record in data['results']:
#             serial_number = record.get('serial_number', '')
#             name = record.get('name', '')
#             label = record.get('label', '')
#             last_seen = record.get('last_seen', '')
#             last_battery_voltage = record.get('last_battery_voltage', '')

#             print(f"Inserting data: serial_number={serial_number}, name={name}, label={label}, last_seen={last_seen}, last_battery_voltage={last_battery_voltage}")

#             # Execute the query
#             mycursor.execute(insert_query, (serial_number, name, label, last_seen, last_battery_voltage))

#         # Commit the changes
#         mydb.commit()

#         # Close cursor and connection
#         mycursor.close()
#         mydb.close()

#         print("Data inserted into the database.")

# if __name__ == "__main__":
#     url =  "https://garden.inajar.nl/api/devices/?format=json"
#     access_token = "33bb3b42452306c58ecedc3c86cfae28ba22329c"  # Replace this with your actual access token
    

#     # access_token = "33bb3b42452306c58ecedc3c86cfae28ba22329c"

#     # You can change the repeat_count to control how many times you want to repeat the process
#     # repeat_count = 10

    
#     fetch_and_display_all(url, access_token)


import sys
from os.path import dirname, abspath, join

# Voeg het pad naar de 'root' directory toe aan sys.path
root_dir = dirname(dirname(abspath(__file__)))
sys.path.append(root_dir)

# Nu kan je de mqtt_client importeren
from mqtt.mqtt_client import create_client, start_loop

# Je kunt nu de create_client en start_loop functies gebruiken

# Lijst waarop je je wil subscriben
mqtt_topics = [
    "goodgarden/devices"
]

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Abonneer op alle topics in de mqtt_topics lijst
    for topic in mqtt_topics:
        client.subscribe(topic)
        print(f"Subscribed to {topic}")

def on_message(client, userdata, msg):
    # Decodeer de payload van bytes naar string
    message = msg.payload.decode()
    print(f"Message received on topic {msg.topic}: {message}")
    # Hier kun je code toevoegen om iets te doen met het ontvangen bericht

if __name__ == "__main__":
    client = create_client("subscriber1", on_connect, on_message)  # Zorg voor een unieke client ID
    start_loop(client)