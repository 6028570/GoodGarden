import requests
import mysql.connector  # Import MySQL connector
from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__, template_folder='src/py/templates', static_folder='src/py/static')
CORS(app)
# Function to get data from the API
def get_api_data():
    api_url = "https://garden.inajar.nl/api/battery_voltage_events/?format=json"
    access_token = "33bb3b42452306c58ecedc3c86cfae28ba22329c"  # Replace this with your actual access token

    headers = {"Authorization": f"Token {access_token}"}
    response = requests.get(api_url, headers=headers)

    if response.ok:
        return response.json().get('results', [])
    else:
        print(f"Error fetching data from the API. Status code: {response.status_code}")
        return []

# Function to get data from the MySQL database
def get_database_data():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='goodgarden'  # Specify the correct database name here
    )
    cursor = connection.cursor()

    # Query to retrieve the latest battery voltage data
    query = "SELECT timestamp, gateway_receive_time, device, value FROM battery_voltage_events ORDER BY timestamp DESC LIMIT 1"
    cursor.execute(query)
    battery_data = cursor.fetchone()

    connection.close()

    return battery_data


@app.route('/')
def index():
    # Get data from the API
    api_data = get_api_data()
    print("API Data:", api_data)  # Add this line for debugging

    # Get data from the database
    battery_data = get_database_data()
    print("Battery Data:", battery_data)  # Add this line for debugging

    # Pass data to the HTML template, including the latest ID
    return render_template('kas_informatie.html', api_data=api_data, battery_data=battery_data)  # Pass the latest_id to the template

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)