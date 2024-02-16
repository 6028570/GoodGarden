import requests
import time

from db_connect import database_connect

def fetch_and_display_all(urls, access_token):
    for url in urls:
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
        time.sleep(300)  # Time here is in seconds.

def load_data(data):
    mydb = database_connect()
    if mydb.is_connected():
        mycursor = mydb.cursor()

        # Here you need to adjust the correct column names and data formats based on the API response
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

            # Execute the query
            mycursor.execute(insert_query, (serial_number, name, label, last_seen, last_battery_voltage))

        # Commit the changes
        mydb.commit()

        # Close cursor and connection
        mycursor.close()
        mydb.close()

        print("Data inserted into the database.")

if __name__ == "__main__":
    urls = [
        "https://garden.inajar.nl/api/devices/?format=json"
    ]
    
    access_token = "33bb3b42452306c58ecedc3c86cfae28ba22329c"
    
    fetch_and_display_all(urls, access_token)
