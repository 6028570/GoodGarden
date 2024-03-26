from flask import Flask, jsonify, request, redirect, url_for
import mysql.connector

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

@app.route('/care_schedules', methods=['GET'])
def get_care_schedules():
    care_schedules_data = get_care_schedules_data()

    if care_schedules_data is None:
        return jsonify({"error": "Kan verzorgingsschema-gegevens niet ophalen uit de database"})

    return jsonify(care_schedules_data)

# Flask route om het formulier voor het toevoegen van een nieuwe plant te verwerken
@app.route('/add_plant', methods=['POST'])
def add_plant():
    if request.method == 'POST':
        try:
            plant_naam = request.form['plant_naam']  # Hier wordt de plantnaam uit het formulier gehaald
            plantensoort = request.form['plantensoort']
            plant_geteelt = request.form['plant_geteelt']

            # Voeg de nieuwe plant toe aan de database
            if add_plant_to_database(plant_naam, plantensoort, plant_geteelt):
                return redirect(url_for('get_plants'))  # Redirect naar de pagina met de lijst van planten
            else:
                return jsonify({"error": "Fout bij het toevoegen van de plant aan de database"}), 500
        except Exception as e:
            print("Fout bij het toevoegen van de plant:", e)
            return jsonify({"error": "Fout bij het toevoegen van de plant"}), 500

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
