from flask import Flask, jsonify, request
import mysql.connector
import requests

app = Flask(__name__)

# Functie om data op te halen uit de MySQL-database voor batterij voltage events
def get_battery_voltage_data():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='goodgarden'
        )
        cursor = connection.cursor()

        # Query om data op te halen uit de battery_voltage_events-tabel
        query = "SELECT id, timestamp, gateway_receive_time, device, value FROM battery_voltage_events ORDER BY timestamp DESC LIMIT 1"
        cursor.execute(query)
        battery_voltage_data = cursor.fetchone()

        connection.close()

        return battery_voltage_data
    except Exception as e:
        print("Fout bij het ophalen van batterij voltage gegevens uit de database:", e)
        return None

# Functie om data op te halen uit de MySQL-database voor planten
def get_plants_data():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='goodgarden'
        )
        cursor = connection.cursor()

        # Query om data op te halen uit de plants-tabel
        query = "SELECT id, name, type, beschrijving, licht, vochtigheid FROM plants"
        cursor.execute(query)
        plants_data = cursor.fetchall()

        connection.close()

        return plants_data
    except Exception as e:
        print("Fout bij het ophalen van plantgegevens uit de database:", e)
        return None

# Functie om data op te halen uit de MySQL-database voor care schedules
def get_care_schedules_data():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='goodgarden'
        )
        cursor = connection.cursor()

        # Query om data op te halen uit de care_schedules-tabel
        query = "SELECT plant_id, water, bemesting FROM care_schedules"
        cursor.execute(query)
        care_schedules_data = cursor.fetchall()

        connection.close()

        return care_schedules_data
    except Exception as e:
        print("Fout bij het ophalen van care schedule gegevens uit de database:", e)
        return None

# Functie om een nieuwe plant toe te voegen aan de database
def add_plant_to_database(plant_naam, plantensoort, plant_geteelt):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='goodgarden'
        )
        cursor = connection.cursor()

        # Query om een nieuwe plant toe te voegen aan de plants-tabel
        query = "INSERT INTO plants (name, type, beschrijving, licht, vochtigheid) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (plant_naam, plantensoort, '', '', ''))  # Beschrijving, licht en vochtigheid kunnen leeg blijven
        connection.commit()

        connection.close()
        return True
    except Exception as e:
        print("Fout bij het toevoegen van de plant aan de database:", e)
        return False

def get_weather_data():
    api_key = "05ddd06644"
    location = "Leiden"
    url = f"https://weerlive.nl/api/weerlive_api_v2.php?key={api_key}&locatie={location}"
    response = requests.get(url).json()
    return response

@app.route('/weather', methods=['GET'])
def get_weather():
    weather_response = get_weather_data()

    if 'error' in weather_response:
        return jsonify({"error": "Kon weerdata niet ophalen"})

    live_weather = weather_response.get('liveweer', [])
    today_forecast = weather_response.get('verwachting_vandaag', [])

    weather_data = {
        "live_weather": live_weather[0] if live_weather else {},
        "today_forecast": today_forecast[0] if today_forecast else {}
    }

    return jsonify(weather_data)

@app.route('/battery_voltage_events', methods=['GET'])
def get_battery_voltage_events():
    battery_voltage_data = get_battery_voltage_data()

    if battery_voltage_data is None:
        return jsonify({"error": "Kan batterijspanningsgegevens niet ophalen uit de database"})

    response = {
        "id": battery_voltage_data[0],
        "timestamp": str(battery_voltage_data[1]),  
        "gateway_receive_time": str(battery_voltage_data[2]), 
        "device": battery_voltage_data[3],
        "value": battery_voltage_data[4]
    }

    return jsonify(response)

@app.route('/plants', methods=['GET'])
def get_plants():
    plants_data = get_plants_data()

    if plants_data is None:
        return jsonify({"error": "Kan plantgegevens niet ophalen uit de database"})

    return jsonify(plants_data)

@app.route('/plants/<string:plant_name>', methods=['GET'])
def get_plant_by_name(plant_name):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='goodgarden'
        )
        cursor = connection.cursor()

        # Query om data op te halen voor een specifieke plantnaam
        query = "SELECT id, name, type, beschrijving, licht, vochtigheid FROM plants WHERE name = %s"
        cursor.execute(query, (plant_name,))
        plant_data = cursor.fetchone()

        connection.close()

        if plant_data:
            return jsonify({
                "id": plant_data[0],
                "name": plant_data[1],
                "type": plant_data[2],
                "beschrijving": plant_data[3],
                "licht": plant_data[4],
                "vochtigheid": plant_data[5]
            })
        else:
            return jsonify({"error": "Plant not found"}), 404
    except Exception as e:
        print("Error retrieving plant data from database:", e)
        return jsonify({"error": "Failed to retrieve plant data"}), 500

@app.route('/care_schedules', methods=['GET'])
def get_care_schedules():
    care_schedules_data = get_care_schedules_data()

    if care_schedules_data is None:
        return jsonify({"error": "Kan verzorgingsschema-gegevens niet ophalen uit de database"})

    return jsonify(care_schedules_data)

@app.route('/add_plant', methods=['POST'])
def add_plant():
    data = request.get_json()
    plant_name = data.get('name', '')
    plant_type = data.get('type', '')
    plant_grown = data.get('geteelt', '')

    if add_plant_to_database(plant_name, plant_type, plant_grown):
        return jsonify({"message": "Plant toegevoegd aan de database"})
    else:
        return jsonify({"error": "Kon de plant niet toevoegen aan de database"})

if __name__ == '__main__':
    app.run(debug=True)
