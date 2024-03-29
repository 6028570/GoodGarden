from flask import Flask, jsonify
import mysql.connector
 
app = Flask(__name__)
 
# Function to get data from the MySQL database
def get_database_data():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='goodgarden'
        )
        cursor = connection.cursor()
 
        # Query to retrieve the latest battery voltage data
        query = "SELECT id, timestamp, gateway_receive_time, device, value FROM battery_voltage_events ORDER BY timestamp DESC LIMIT 1"
        cursor.execute(query)
        battery_data = cursor.fetchone()
 
        connection.close()
 
        return battery_data
    except Exception as e:
        print("Error fetching data from database:", e)
        return None
 
@app.route('/', methods=['GET'])
def get_data():
    # Get data from the database
    battery_data = get_database_data()
 
    if battery_data is None:
        return jsonify({"error": "Failed to fetch data from database"})
 
    # Convert the fetched data into a dictionary
    data_dict = {
        "id": battery_data[0],
        "timestamp": str(battery_data[1]),  # Convert timestamp to string for JSON serialization
        "gateway_receive_time": str(battery_data[2]),  # Convert timestamp to string for JSON serialization
        "device": battery_data[3],
        "value": battery_data[4]
    }
 
    # Return the data as JSON
    return jsonify(data_dict)
 
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)