import mysql.connector
import requests
import time

# Function to make a connection to the database
def database_connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="goodgarden"
    )

# Function for creating data in the database based on battery voltage information from the API
def create_data_from_api(url, access_token, repeat_count=5):
    for _ in range(repeat_count):
        try:
            headers = {
                "Authorization": f"Token {access_token}"
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            data = response.json()
            insert_data(data['results'])

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {url}: {e}")

        # Wait for a certain time (e.g., 1 second) before making the next API call
        print("Waiting for the next create action...")
        time.sleep(1)

# Function for inserting data into the database
def insert_data(data):
    mydb = database_connect()
    if mydb.is_connected():
        mycursor = mydb.cursor()

        # Adjust column names and data format based on the API response
        insert_query = """
        INSERT INTO goodgarden.battery_voltage_events (timestamp, gateway_receive_time, device, value)
        VALUES (%s, %s, %s, %s)
        """
        for record in data:
            timestamp = record.get('timestamp', '')
            gateway_receive_time = record.get('gateway_receive_time', '')
            device = record.get('device', '')
            value = record.get('value', '')

            print(f"Inserting data: timestamp={timestamp}, gateway_receive_time={gateway_receive_time}, device={device}, value={value}")
            
            # Execute the query
            mycursor.execute(insert_query, (timestamp, gateway_receive_time, device, value))

        # Confirm the changes
        mydb.commit()

        # Close cursor and connection
        mycursor.close()
        mydb.close()

        print("Data inserted into the database.")
# Functie voor het aanmaken van gegevens in de database op basis van batterijspanningsinformatie
def create_data_from_battery_info(battery_info, repeat_count=5):
    for _ in range(repeat_count):
        try:
            # Hier moet je de juiste kolomnamen en gegevensindeling aanpassen op basis van de API-respons
            insert_query = """
            INSERT INTO goodgarden.battery_voltage_events (timestamp, gateway_receive_time, device, value)
            VALUES (%s, %s, %s, %s)
            """

            mydb = database_connect()
            if mydb.is_connected():
                mycursor = mydb.cursor()

                for record in battery_info:
                    timestamp = record.get('timestamp', '')
                    gateway_receive_time = record.get('gateway_receive_time', '')
                    device = record.get('device', '')
                    value = record.get('value', '')

                    print(f"Inserting data: timestamp={timestamp}, gateway_receive_time={gateway_receive_time}, device={device}, value={value}")  # Print de ingevoerde gegevens

                    # Voer de query uit
                    mycursor.execute(insert_query, (timestamp, gateway_receive_time, device, value))

                    # Controleer of de batterijspanning lager is dan 4.5 volt en geef een melding
                    if float(value) < 3.4:
                        print("Waarschuwing: Batterijspanning is lager dan 3.4 volt. Opladen aanbevolen.")
                    # Controleer of de batterijspanning hoger is dan 4.3 volt en geef een melding
                    elif float(value) > 3.9:
                        print("Melding: Batterijspanning is hoger dan 3.9 volt. Batterij is vol.")


                # Bevestig de wijzigingen
                mydb.commit()

                # Sluit cursor en verbinding
                mycursor.close()
                mydb.close()

                print("Data inserted into the database.")

        except mysql.connector.Error as e:
            print(f"Error inserting data into the database: {e}")

        # Wacht een bepaalde tijd (bijv. 1 seconde) voordat de volgende oproep wordt gedaan
        print("Waiting for the next create action...")
        time.sleep(1)


# Function for reading data from the database
def read_data(url, access_token, repeat_count=5):
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

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {url}: {e}")

        # Wait for a certain time (e.g., 1 second) before making the next API call
        print("Waiting for the next read action...")
        time.sleep(300)

# Function for updating data in the database
def update_data(record_id):
    try:
        mydb = database_connect()

        if mydb.is_connected():
            mycursor = mydb.cursor()

            mycursor.execute("SELECT * FROM goodgarden.battery_voltage_events WHERE id = %s", (record_id,))
            existing_record = mycursor.fetchone()

            if not existing_record:
                print(f"Record with ID {record_id} not found. Update operation aborted.")
                return

            new_timestamp = input("Enter new timestamp: ")
            new_gateway_receive_time = input("Enter new gateway_receive_time: ")
            new_device = input("Enter new device: ")
            new_value = input("Enter new value: ")

            update_query = """
            UPDATE goodgarden.battery_voltage_events
            SET timestamp = %s, gateway_receive_time = %s, device = %s, value = %s
            WHERE id = %s
            """

            print(f"Executing update query: {update_query}")
            print(f"Updating record with ID {record_id} to new values - timestamp: {new_timestamp}, gateway_receive_time: {new_gateway_receive_time}, device: {new_device}, value: {new_value}")

            mycursor.execute(update_query, (new_timestamp, new_gateway_receive_time, new_device, new_value, record_id))

            mydb.commit()

            print(f"Update executed. Rowcount: {mycursor.rowcount}")

    except mysql.connector.Error as update_err:
        print(f"Error updating data: {update_err}")
    finally:
        if 'mycursor' in locals() and mycursor is not None:
            mycursor.close()
        if 'mydb' in locals() and mydb.is_connected():
            mydb.close()

# Function for deleting data from the database
def delete_data(record_id):
    mydb = database_connect()
    if mydb.is_connected():
        mycursor = mydb.cursor()

        delete_query = """
        DELETE FROM goodgarden.battery_voltage_events
        WHERE id = %s
        """

        mycursor.execute(delete_query, (record_id,))

        mydb.commit()

        mycursor.close()
        mydb.close()

        print(f"Data with ID {record_id} deleted.")

if __name__ == "__main__":
    url = "https://garden.inajar.nl/api/battery_voltage_events/?format=json"
    access_token = "33bb3b42452306c58ecedc3c86cfae28ba22329c"  # Replace this with your actual access token
    repeat_count = 10

    operation_choice = input("Choose operation (C for Create, R for Read, U for Update, D for Delete): ").upper()

    if operation_choice == "C":
        create_data_from_api(url, access_token, repeat_count)
    elif operation_choice == "R":
        read_data(url, access_token, repeat_count)
    elif operation_choice == "U":
        record_id = int(input("Enter record ID to update: "))
        update_data(record_id)
    elif operation_choice == "D":
        record_id = int(input("Enter record ID to delete: "))
        delete_data(record_id)
    else:
        print("Invalid operation choice. Please choose C, R, U, or D.")
