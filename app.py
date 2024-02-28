from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Functie om gegevens van de API op te halen
def get_api_data():
    api_url = "https://garden.inajar.nl/api/battery_voltage_events/?format=json"
    access_token = "33bb3b42452306c58ecedc3c86cfae28ba22329c"  # Vervang dit met je echte toegangstoken

    headers = {"Authorization": f"Token {access_token}"}
    response = requests.get(api_url, headers=headers)

    if response.ok:
        return response.json().get('results', [])
    else:
        print(f"Fout bij het ophalen van gegevens van de API. Statuscode: {response.status_code}")
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/battery_voltage_events')
def battery_voltage_events():
    # Haal gegevens op van de API
    api_data = get_api_data()

    # Return de gegevens als JSON naar de frontend
    return jsonify(results=api_data)

if __name__ == "__main__":
    app.run(debug=True)
