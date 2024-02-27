import mysql.connector
import requests
import time

# Functie om verbinding te maken met de database
def database_connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="goodgarden"
    )

# Functie voor het aanmaken van gegevens in de database
def create_data(url, access_token, repeat_count=5):
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
            insert_data(data)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {url}: {e}")

        # Wacht een bepaalde tijd (bijv. 1 seconde) voordat de volgende oproep wordt gedaan
        print("Waiting for the next create action...")
        time.sleep(1)

# Functie voor het invoegen van gegevens in de database
def insert_data(data):
    mydb = database_connect()
    if mydb.is_connected():
        mycursor = mydb.cursor()

        # Hier moet je de juiste kolomnamen en gegevensindeling aanpassen op basis van de API-respons
        insert_query = """
        INSERT INTO goodgarden.battery_voltage_events (timestamp, gateway_receive_time, device, value)
        VALUES (%s, %s, %s, %s)
        """
        for record in data['results']:  # Pas dit aan op basis van de werkelijke structuur van de JSON
            timestamp = record.get('timestamp', '')
            gateway_receive_time = record.get('gateway_receive_time', '')
            device = record.get('device', '')
            value = record.get('value', '')

            print(f"Inserting data: timestamp={timestamp}, gateway_receive_time={gateway_receive_time}, device={device}, value={value}")  # Print de ingevoerde gegevens

            # Voer de query uit
            mycursor.execute(insert_query, (timestamp, gateway_receive_time, device, value))

        # Bevestig de wijzigingen
        mydb.commit()

        # Sluit cursor en verbinding
        mycursor.close()
        mydb.close()

        print("Data inserted into the database.")

# Functie voor het lezen van gegevens uit de database
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

        # Wacht een bepaalde tijd (bijv. 1 seconde) voordat de volgende oproep wordt gedaan
        print("Waiting for the next read action...")
        time.sleep(300)

# Functie voor het bijwerken van gegevens in de database
def update_data(record_id):
    try:
        mydb = database_connect()

        if mydb.is_connected():
            mycursor = mydb.cursor()

            # Controleer of het record bestaat voordat je het bijwerkt
            mycursor.execute("SELECT * FROM goodgarden.battery_voltage_events WHERE id = %s", (record_id,))
            existing_record = mycursor.fetchone()

            if not existing_record:
                print(f"Record with ID {record_id} not found. Update operation aborted.")
                return

            # Vraag de gebruiker om nieuwe waarden voor de andere velden
            new_timestamp = input("Enter new timestamp: ")
            new_gateway_receive_time = input("Enter new gateway_receive_time: ")
            new_device = input("Enter new device: ")
            new_value = input("Enter new value: ")

            # Hier moet je de juiste kolomnamen aanpassen op basis van de structuur van je database
            update_query = """
            UPDATE goodgarden.battery_voltage_events
            SET timestamp = %s, gateway_receive_time = %s, device = %s, value = %s
            WHERE id = %s
            """

            # Voer de query uit
            print(f"Executing update query: {update_query}")
            print(f"Updating record with ID {record_id} to new values - timestamp: {new_timestamp}, gateway_receive_time: {new_gateway_receive_time}, device: {new_device}, value: {new_value}")

            mycursor.execute(update_query, (new_timestamp, new_gateway_receive_time, new_device, new_value, record_id))

            # Bevestig de wijzigingen
            mydb.commit()

            print(f"Update executed. Rowcount: {mycursor.rowcount}")

    except mysql.connector.Error as update_err:
        print(f"Error updating data: {update_err}")
    finally:
        # Zorg ervoor dat je altijd de cursor en de databaseverbinding sluit
        if 'mycursor' in locals() and mycursor is not None:
            mycursor.close()
        if 'mydb' in locals() and mydb.is_connected():
            mydb.close()
            

# Functie voor het verwijderen van gegevens uit de database
def delete_data(record_id):
    mydb = database_connect()
    if mydb.is_connected():
        mycursor = mydb.cursor()

        # Hier moet je de juiste kolomnamen aanpassen op basis van de structuur van je database
        delete_query = """
        DELETE FROM goodgarden.battery_voltage_events
        WHERE id = %s
        """

        # Voer de query uit
        mycursor.execute(delete_query, (record_id,))

        # Bevestig de wijzigingen
        mydb.commit()

        # Sluit cursor en verbinding
        mycursor.close()
        mydb.close()

        print(f"Data with ID {record_id} deleted.")

if __name__ == "__main__":
    url = "https://garden.inajar.nl/api/battery_voltage_events/?format=json"
    access_token = "33bb3b42452306c58ecedc3c86cfae28ba22329c"  # Vervang dit door je werkelijke toegangstoken
    
    # Je kunt repeat_count wijzigen om te bepalen hoe vaak je de bewerking wilt herhalen
    repeat_count = 10
    
    # Keuze voor de bewerking
    operation_choice = input("Choose operation (C for Create, R for Read, U for Update, D for Delete): ").upper()

    if operation_choice == "C":
        # Maak gegevens aan
        create_data(url, access_token, repeat_count)
    elif operation_choice == "R":
        # Lees gegevens
        read_data(url, access_token, repeat_count)
    elif operation_choice == "U":
        # Update gegevens
        record_id = int(input("Enter record ID to update: "))
        # Call the update_data function without additional arguments
        update_data(record_id)
    elif operation_choice == "D":
        # Verwijder gegevens
        record_id = int(input("Enter record ID to delete: "))
        delete_data(record_id)
    else:
        print("Invalid operation choice. Please choose C, R, U, or D.")