import mysql.connector
import requests
import time

def gegevens_ophalen_en_database_bijwerken():
    # API-verzoek
    url = "https://garden.inajar.nl/api/battery_voltage_events/?format=json"
    headers = {
        "Authorization": "Token 33bb3b42452306c58ecedc3c86cfae28ba22329c"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json().get('results', [])

        print("API-reactie:")
        print(data)

        if not isinstance(data, list):
            raise ValueError("De API-reactie wordt niet herkend als een lijst van dictionaries.")

        # Verbinding maken met de database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="goodgarden"
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Database bijwerken met API-gegevens
            for entry in data:
                timestamp = entry.get("timestamp")
                gateway_receive_time = entry.get("gateway_receive_time")
                device = entry.get("device")
                value = entry.get("value")

                # Veronderstel dat de kolommen van de 'sensor_data'-tabel timestamp, gateway_receive_time, device, en value zijn
                sql_update_query = f"INSERT INTO goodgarden.sensor_data (timestamp, gateway_receive_time, device, value) VALUES ({timestamp}, '{gateway_receive_time}', {device}, {value})"
                cursor.execute(sql_update_query)
                connection.commit()

            print("Database succesvol bijgewerkt")

    except Exception as e:
        print(f"Fout bijwerken database: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL-verbinding is gesloten")

# Zet een timer op om de functie elke 10 minuten uit te voeren
while True:
    gegevens_ophalen_en_database_bijwerken()
    time.sleep(60)  # 600 seconden = 10 minuten
