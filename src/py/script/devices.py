import json
from db_connect import database_connect
from paho.mqtt import subscribe

def on_message(client, userdata, message):
    payload_str = message.payload.decode("utf-8")
    data = json.loads(payload_str)

    # Verbinding maken met de database
    mydb = database_connect()

    if mydb.is_connected():
        
        # Creëren van een cursor object
        mycursor = mydb.cursor()

        # SQL query voor het invoegen van de gegevens
        insert_query = """
        INSERT INTO goodgarden.devices
        (serial_number, name, label, last_seen, last_battery_voltage, device_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        # Verwerken van de gegevens uit het bericht
        for record in data['results']:
            serial_number = record.get('serial_number', '')
            name = record.get('name', '')
            label = record.get('label', '')
            last_seen = record.get('last_seen', '')
            last_battery_voltage = record.get('last_battery_voltage', '')
            device_id = record.get("id", "")

            print(f"Inserting data: serial_number={serial_number}, name={name}, label={label}, last_seen={last_seen}, last_battery_voltage={last_battery_voltage}, device_id={device_id}")

            # Uitvoeren van de SQL query
            mycursor.execute(insert_query, (serial_number, name, label, last_seen, last_battery_voltage, device_id))

        # Commit de transacties naar de database
        mydb.commit()

        # Sluiten van de cursor en de databaseconnectie
        mycursor.close()
        mydb.close()

        print("Data inserted into the database.")

    else:
        print("Failed to connect to the database.")

    print(f"\033[92mMessage received on topic\033[0m {message.topic}: {data}")

if __name__ == "__main__":
    topic = "goodgarden/devices"
    subscribe.callback(on_message, topic)
