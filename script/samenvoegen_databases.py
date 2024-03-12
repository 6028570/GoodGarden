import requests
import time

from db_connect import database_connect

##########################* DEVICES #######################

def fetch_and_display_all(url, access_token):

    try:
         headers = {
             "Authorization": f"Token {access_token}"
         }
         response = requests.get(url, headers=headers)
         response.raise_for_status()
         data = response.json()
         print(f"Data from {url}:")
         print(data)
         load_data(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        print("Waiting for the next retrieval action...")

    time.sleep(1)

def load_data(data):
    mydb = database_connect()
    if mydb.is_connected():
        mycursor = mydb.cursor()

        insert_query = """
        INSERT INTO goodgarden.devices (serial_number, name, label, last_seen, last_battery_voltage)
        VALUES (%s, %s, %s, %s, %s )
        """
        for record in data['results']:
            serial_number = record.get('serial_number', '')
            name = record.get('name', '')
            label = record.get('label', '')
            last_seen = record.get('last_seen', '')
            last_battery_voltage = record.get('last_battery_voltage', '')

            print(f"Inserting data: serial_number={serial_number}, name={name}, label={label}, last_seen={last_seen}, last_battery_voltage={last_battery_voltage}")

            mycursor.execute(insert_query, (serial_number, name, label, last_seen, last_battery_voltage))

        mydb.commit()

        mycursor.close()
        mydb.close()

        print("Data inserted into the database.")

if __name__ == "__main__":
    url =  "https://garden.inajar.nl/api/devices/?format=json"
    access_token = "33bb3b42452306c58ecedc3c86cfae28ba22329c"  
    
    fetch_and_display_all(url, access_token)

############################### EINDE ########################
    #                                                   #
    #                                                   #
    #                                                   #  
    #                                                   #
##########################* PAR_EVENTS #######################

import requests
import time

from db_connect import database_connect

def fetch_and_display_all(url, access_token, repeat_count=5):
    for _ in range(repeat_count):
        try:
            headers = {
                "Authorization": f"Token {access_token}"
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            data = response.json()
            print(f"Data from {url}:")
            print(data)
            load_data(data)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {url}: {e}")

        print("Waiting for the next retrieval action...")

        time.sleep(1)  # Time here is in seconds.


def load_data(data):
    mydb = database_connect()
    if mydb.is_connected():
        mycursor = mydb.cursor()

        # Here you need to adjust the correct column names and data formats based on the API response
        insert_query = """
        INSERT INTO goodgarden.par_events (timestamp, gateway_receive_time, device, value)
        VALUES (%s, %s, %s, %s)
        """
        for record in data['results']:
            timestamp = record.get('timestamp', '')
            gateway_receive_time = record.get('gateway_receive_time', '')
            device = record.get('device', '')
            value = record.get('value', '')

            print(f"Inserting data: timestamp={timestamp}, gateway_receive_time={gateway_receive_time}, device={device}, value={value}")

            # Execute the query
            mycursor.execute(insert_query, (timestamp, gateway_receive_time, device, value))

        # Commit the changes
        mydb.commit()

        # Close cursor and connection
        mycursor.close()
        mydb.close()

        print("Data inserted into the database.")

if __name__ == "__main__":
    url =  "https://garden.inajar.nl/api/par_events/?format=json"
    access_token = "33bb3b42452306c58ecedc3c86cfae28ba22329c"  
    # You can change the repeat_count to control how many times you want to repeat the process
    repeat_count = 10
    
    fetch_and_display_all(url, access_token, repeat_count)

############################### EINDE ########################
    #                                                   #
    #                                                   #
    #                                                   #  
    #                                                   #
##########################* RELATIVE_HUMIDITY_EVENTS #######################
    
import requests
import time

from db_connect import database_connect

def fetch_and_display_all(url, access_token, repeat_count=5):
    for _ in range(repeat_count):
        try:
            headers = {
                "Authorization": f"Token {access_token}"
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            data = response.json()
            print(f"Data from {url}:")
            print(data)
            load_data(data)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {url}: {e}")

        print("Waiting for the next retrieval action...")

        time.sleep(1)  # Time here is in seconds.

def load_data(data):
    mydb = database_connect()
    if mydb.is_connected():
        mycursor = mydb.cursor()

        # Here you need to adjust the correct column names and data formats based on the API response
        insert_query = """
        INSERT INTO goodgarden.relative_humidity_events (timestamp, gateway_receive_time, device, value)
        VALUES (%s, %s, %s, %s)
        """
        for record in data['results']:
            timestamp = record.get('timestamp', '')
            gateway_receive_time = record.get('gateway_receive_time', '')
            device = record.get('device', '')
            value = record.get('value', '')

            print(f"Inserting data: timestamp={timestamp}, gateway_receive_time={gateway_receive_time}, device={device}, value={value}")

            # Execute the query
            mycursor.execute(insert_query, (timestamp, gateway_receive_time, device, value))

        # Commit the changes
        mydb.commit()

        # Close cursor and connection
        mycursor.close()
        mydb.close()

        print("Data inserted into the database.")

if __name__ == "__main__":
    url = "https://garden.inajar.nl/api/relative_humidity_events/?format=json"
    access_token = "33bb3b42452306c58ecedc3c86cfae28ba22329c"
    
    # You can change the repeat_count to control how many times you want to repeat the process
    repeat_count = 10
    
    fetch_and_display_all(url, access_token, repeat_count)

############################### EINDE ########################
    #                                                   #
    #                                                   #
    #                                                   #  
    #                                                   #
##########################* SOIL_ELECTRIC_CONDUCTIVITY_EVENTS #######################
    
import requests
import time

from db_connect import database_connect

def fetch_and_display_all(url, access_token, repeat_count=5):
    for _ in range(repeat_count):
        try:
            headers = {
                "Authorization": f"Token {access_token}"
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            data = response.json()
            print(f"Data from {url}:")
            print(data)
            load_data(data)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {url}: {e}")

        print("Waiting for the next retrieval action...")

        time.sleep(1)  # Time here is in seconds.

def load_data(data):
    mydb = database_connect()
    if mydb.is_connected():
        mycursor = mydb.cursor()

        # Here you need to adjust the correct column names and data formats based on the API response
        insert_query = """
        INSERT INTO goodgarden.soil_electric_conductivity_events (timestamp, gateway_receive_time, device, value)
        VALUES (%s, %s, %s, %s)
        """
        for record in data['results']:
            timestamp = record.get('timestamp', '')
            gateway_receive_time = record.get('gateway_receive_time', '')
            device = record.get('device', '')
            value = record.get('value', '')

            print(f"Inserting data: timestamp={timestamp}, gateway_receive_time={gateway_receive_time}, device={device}, value={value}")

            # Execute the query
            mycursor.execute(insert_query, (timestamp, gateway_receive_time, device, value))

        # Commit the changes
        mydb.commit()

        # Close cursor and connection
        mycursor.close()
        mydb.close()

        print("Data inserted into the database.")
if __name__ == "__main__":
    url = "https://garden.inajar.nl/api/soil_electric_conductivity_events/?format=json"
    access_token = "33bb3b42452306c58ecedc3c86cfae28ba22329c"  # Replace this with your actual access token

    # You can change the repeat_count to control how many times you want to repeat the process
    repeat_count = 10
    
    fetch_and_display_all(url, access_token, repeat_count)

############################### EINDE ########################
    #                                                   #
    #                                                   #
    #                                                   #  
    #                                                   #
##########################* SOIL_TEMPERATURE_EVENTS #######################

import requests
import time

from db_connect import database_connect

def fetch_and_display_all(url, access_token, repeat_count=5):
    for _ in range(repeat_count):
        try:
            headers = {
                "Authorization": f"Token {access_token}"
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            data = response.json()
            print(f"Data from {url}:")
            print(data)
            load_data(data)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {url}: {e}")

        print("Waiting for the next retrieval action...")

        time.sleep(1)  # Time here is in seconds.


def load_data(data):
    mydb = database_connect()
    if mydb.is_connected():
        mycursor = mydb.cursor()

        # Here you need to adjust the correct column names and data formats based on the API response
        insert_query = """
        INSERT INTO goodgarden.soil_temperature_events (timestamp, gateway_receive_time, device, value)
        VALUES (%s, %s, %s, %s)
        """
        for record in data['results']:
            timestamp = record.get('timestamp', '')
            gateway_receive_time = record.get('gateway_receive_time', '')
            device = record.get('device', '')
            value = record.get('value', '')

            print(f"Inserting data: timestamp={timestamp}, gateway_receive_time={gateway_receive_time}, device={device}, value={value}")

            # Execute the query
            mycursor.execute(insert_query, (timestamp, gateway_receive_time, device, value))

        # Commit the changes
        mydb.commit()

        # Close cursor and connection
        mycursor.close()
        mydb.close()

        print("Data inserted into the database.")

if __name__ == "__main__":
    url = "https://garden.inajar.nl/api/soil_relative_permittivity_events/?format=json"
    access_token = "33bb3b42452306c58ecedc3c86cfae28ba22329c"  
    # You can change the repeat_count to control how many times you want to repeat the process
    repeat_count = 10
    
    # fetch_and_display_all(urls, access_token)

    fetch_and_display_all(url, access_token, repeat_count)

############################### EINDE ########################
    #                                                   #
    #                                                   #
    #                                                   #  
    #                                                   #
##########################* SOIL_TEMPERATURE_EVENTS #######################
    
    import requests
import time

from db_connect import database_connect

def fetch_and_display_all(url, access_token, repeat_count=5):
    for _ in range(repeat_count):

        try:
            headers = {
                "Authorization": f"Token {access_token}"
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            data = response.json()
            print(f"Data from {url}:")
            print(data)
            load_data(data)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {url}: {e}")

        print("Waiting for the next retrieval action...")

        time.sleep(1)  # Time here is in seconds.

def load_data(data):
    mydb = database_connect()
    if mydb.is_connected():
        mycursor = mydb.cursor()

        # Here you need to adjust the correct column names and data formats based on the API response
        insert_query = """
        INSERT INTO goodgarden.soil_temperature_events (timestamp, gateway_receive_time, device, value)
        VALUES (%s, %s, %s, %s)
        """
        for record in data['results']:
            timestamp = record.get('timestamp', '')
            gateway_receive_time = record.get('gateway_receive_time', '')
            device = record.get('device', '')
            value = record.get('value', '')

            print(f"Inserting data: timestamp={timestamp}, gateway_receive_time={gateway_receive_time}, device={device}, value={value}")

            # Execute the query
            mycursor.execute(insert_query, (timestamp, gateway_receive_time, device, value))

        # Commit the changes
        mydb.commit()

        # Close cursor and connection
        mycursor.close()
        mydb.close()

        print("Data inserted into the database.")
if __name__ == "__main__":
    url =     "https://garden.inajar.nl/api/soil_temperature_events/?format=json"
    access_token = "33bb3b42452306c58ecedc3c86cfae28ba22329c"  # Replace this with your actual access token

    # You can change the repeat_count to control how many times you want to repeat the process
    repeat_count = 10
    
    fetch_and_display_all(url, access_token, repeat_count)