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

        # Wait for a certain time (e.g., 60 seconds) before making the next call
        print("Waiting for the next retrieval action...")
        time.sleep(10)  # Time here is in seconds.

def load_data(data):
    mydb = database_connect()
    if mydb.is_connected():
        mycursor = mydb.cursor()

        # Here you need to adjust the correct column names and data formats based on the API response
        insert_query = """
        INSERT INTO goodgarden.par_events (timestamp, gateway_receive_time, device, value)
        VALUES (%s, %s, %s, %s)
        """
        for record in data['results']:  # Adjust this based on the actual structure of the JSON
            timestamp = record.get('timestamp', '')
            gateway_receive_time = record.get('gateway_receive_time', '')
            device = record.get('device', '')
            value = record.get('value', '')

            print(f"Inserting data: timestamp={timestamp}, gateway_receive_time={gateway_receive_time}, device={device}, value={value}")  # Print the data being inserted

            # Execute the query
            mycursor.execute(insert_query, (timestamp, gateway_receive_time, device, value))

        # Commit the changes
        mydb.commit()

        # Close cursor and connection
        mycursor.close()
        mydb.close()

        print("Data inserted into the database.")

if __name__ == "__main__":
    urls = [
         "https://garden.inajar.nl/api/par_events/?format=json"
    ]
    
    access_token = "33bb3b42452306c58ecedc3c86cfae28ba22329c"  # Vervang dit met jouw echte toegangstoken
    
    fetch_and_display_all(urls, access_token)
