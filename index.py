import mysql.connector
import requests
import time

while True:
    try:
        # API-verzoek
        url = "https://garden.inajar.nl/api/battery_voltage_events/?format=json"
        headers = {
            "Authorization": "Token 33bb3b42452306c58ecedc3c86cfae28ba22329c"
        }

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

                # Gebruik van prepared statements om SQL-injectie te voorkomen
                sql_update_query = (
                    "UPDATE goodgarden.sensor_data "
                    "SET timestamp=%s, gateway_receive_time=%s, device=%s "
                    "WHERE value=%s"
                )
                cursor.execute(sql_update_query, (timestamp, gateway_receive_time, device, value))
                connection.commit()

            print("Database succesvol bijgewerkt")

    except Exception as e:
        print(f"Fout bijwerken database: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL-verbinding is gesloten")

    # Voeg deze regel toe binnen de while-loop
    print("Aantal gegevens uit de API:", len(data))

    # Voeg een pauze toe van 10 minuten voordat de lus opnieuw wordt uitgevoerd
    time.sleep(600)
