import mysql.connector
import requests
import time

def database_connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="goodgarden"
    )

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

        # Wait for a certain time (e.g., 60 seconds) before making the next call
        print("Waiting for the next retrieval action...")
        time.sleep(1)  # Time here is in seconds.

def load_data(data):
    mydb = database_connect()
    if mydb.is_connected():
        mycursor = mydb.cursor()

        # Here you need to adjust the correct column names and data formats based on the API response
        insert_query = """
        INSERT INTO goodgarden.devices (serial_number, name, label, last_seen, last_battery_voltage)
        VALUES (%s, %s, %s, %s, %s )
        """
        for record in data['results']:  # Adjust this based on the actual structure of the JSON
            serial_number = record.get('serial_number', '')
            name = record.get('name', '')
            label = record.get('label', '')
            last_seen = record.get('last_seen', '')
            last_battery_voltage = record.get('last_battery_voltage', '')

            print(f"Inserting data: serial_number={serial_number}, name={name}, label={label}, last_seen={last_seen}, last_battery_voltage={last_battery_voltage}")  # Print the data being inserted

            # Execute the query
            mycursor.execute(insert_query, (serial_number, name, label, last_seen, last_battery_voltage))


        # Commit the changes
        mydb.commit()

        # Close cursor and connection
        mycursor.close()
        mydb.close()

        print("Data inserted into the database.")

if __name__ == "__main__":
    url =  "https://garden.inajar.nl/api/devices/?format=json"
    access_token = "33bb3b42452306c58ecedc3c86cfae28ba22329c"  # Replace this with your actual access token
    
    # You can change the repeat_count to control how many times you want to repeat the process
    repeat_count = 10
    
    fetch_and_display_all(url, access_token, repeat_count)
