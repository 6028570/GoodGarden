from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def database_connect():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='goodgarden'
        )
        return connection
    except Exception as e:
        print("Database connection failed:", e)
        return None


# Function to get data from the MySQL database
def get_database_data():

    mydb = database_connect()

    if mydb and mydb.is_connected():

        cursor = mydb.cursor()

        # Query to retrieve the latest battery voltage data
        query = "SELECT label, last_seen, last_battery_voltage, device_id FROM devices ORDER BY device_id DESC LIMIT 1"
        cursor.execute(query)
        battery_data = cursor.fetchone()
        mydb.close()
        return battery_data
    
# def devices_data():


@app.route('/', methods=['GET'])
def get_data():
    # Get data from the database
    battery_data = get_database_data()

    if battery_data is None:
        return jsonify({"error": "Failed to fetch data from database"})

    # Convert the fetched data into a dictionary
    data_dict = {
        "label": battery_data[0],
        "last_seen": battery_data[1],
        "last_battery_voltage": battery_data[2],
        "device_id": battery_data[3]
    }

    print(data_dict)

    # Return the data as JSON
    return jsonify(data_dict)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
