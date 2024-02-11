import mysql.connector
import requests

# Verbinding maken met de database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="goodgarden"
)

# Controleren of de verbinding succesvol is
if mydb.is_connected():
    print("Connected to the database")
else:
    print("Failed to connect to the database")

try:
    # Maak een cursor aan
    mycursor = mydb.cursor()

    # Voer de query uit om gegevens op te halen
    mycursor.execute("SELECT * FROM goodgarden.sensor_data")

    # Haal de resultaten op
    myresult = mycursor.fetchall()

    # Print de resultaten
    for x in myresult:
        print(x)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Sluit de cursor en de databaseverbinding
    mycursor.close()
    mydb.close(

    )

def fetch_data():
    url = "https://garden.inajar.nl/api/battery_voltage_events/?format=json"
    headers = {
        "Authorization": "Token 33bb3b42452306c58ecedc3c86cfae28ba22329c"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        load_data(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

def load_data(data):
    api_data = data
    print("Data loaded:", api_data)

if __name__ == "__main__":
    fetch_data()
