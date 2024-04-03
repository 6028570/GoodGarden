from flask import Flask, jsonify
import mysql.connector
import requests
 
app = Flask(__name__)
 
def database_connect():
    try:
   
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="goodgarden"
        )
        return connection
   
    except Exception as e:
 
        print("Database connection failed:", e)
        return None
   
 
# Function to get data from the MySQL database
def get_database_data():
    mydb = database_connect()
    if mydb and mydb.is_connected():
   
        cursor = mydb.cursor(dictionary=True) # Enable dictionary result
 
        # Query to retrieve the latest battery voltage data
        query = "SELECT label, last_seen, last_battery_voltage, device_id FROM devices"
        cursor.execute(query)
        battery_data = cursor.fetchall() # Fetch all rows
        mydb.close()
        return battery_data
   
 
@app.route('/', methods=['GET'])
def get_data():
    battery_data = get_database_data()
 
    if battery_data is None or len(battery_data) == 0:
   
        return jsonify({"error": "Failed to fetch data from database"})
 
 
    return jsonify(battery_data) # Directly return the list of dictionaries as JSON
 
 
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
    weather_forecast = weather_response.get('wk_verw', [])
    day_forecast = weather_response.get('wk_verw', [])  # Dagverwachtingen
 
    weather_data = {
        "live_weather": live_weather[0] if live_weather else {},
        "weather_forecast": weather_forecast,
        "day_forecast": day_forecast  # Voeg de dagverwachtingen toe aan de weerdata
    }
 
    return jsonify(weather_data)
 
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)