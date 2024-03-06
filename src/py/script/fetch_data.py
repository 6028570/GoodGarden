import requests
import time

from db_connect import database_connect

def fetch_battery_voltage_events():
    url = "https://garden.inajar.nl/api/battery_voltage_events/?format=json"
    headers = {
        "Authorization": "Token 33bb3b42452306c58ecedc3c86cfae28ba22329c"
    }

    while True:
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            data = response.json()
            load_data(data)

            print("Wachten voor de volgende ophaalactie...")
            time.sleep(300)  # De tijd hier is in seconden.

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            # Wacht ook hier bij een fout, om niet in een snelle foutloop te komen
            time.sleep(300)

def load_data(data):
    mydb = database_connect()
    if mydb.is_connected():
        mycursor = mydb.cursor()

        # Hier moet je de juiste kolomnamen en dataformaten aanpassen op basis van de API-respons
        insert_query = """
        INSERT INTO goodgarden.battery_voltage_events (timestamp, gateway_receive_time, device, value)
        VALUES (%s, %s, %s, %s)
        """
        for record in data['results']:
            timestamp = record['timestamp']
            gateway_receive_time = record['gateway_receive_time']
            device = record['device']
            value = record['value']

        # print(f"Inserting data: timestamp={timestamp}, gateway_receive_time={gateway_receive_time}, device={device}, value={value}")
        mycursor.execute(insert_query, (timestamp, gateway_receive_time, device, value))

        # Commit de wijzigingen
        mydb.commit()

        # Sluit cursor en verbinding
        mycursor.close()
        mydb.close()

        print("Data ingevoegd in de database.")

if __name__ == "__main__":
    fetch_battery_voltage_events()