const { ipcRenderer } = require("electron");
const axios = require('axios');

// Function to open the modal
function openModal() {
    const modal = document.getElementById("myModal");
    const button = document.getElementById("modalButton");
    const close = document.getElementsByClassName("close")[0];

    if (modal && button && close) { // Check if elements are found
        // Toon de modal wanneer op de knop wordt geklikt
        button.onclick = function () {
            modal.style.display = "block";
        }

        // Sluit de modal wanneer op het 'sluiten' icoon wordt geklikt
        close.onclick = function () {
            modal.style.display = "none";
        }

        // Sluit de modal wanneer buiten de modal wordt geklikt
        window.onclick = function (event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }
    } else {
        console.error("Modal elements not found");
    }
}

document.addEventListener('DOMContentLoaded', () => {
    // Call openModal when DOM content is loaded
    openModal();

    // Send a message to the main process to execute the Python script
    ipcRenderer.send('run-python-script', ['some', 'arguments']);

    ipcRenderer.on('python-script-response', (event, pythonData) => {
        if (pythonData === 'error') {
            console.error('An error occurred while retrieving data from Python');
        } else {
            // Update HTML elements with data received from Python
            document.getElementById('bodem-temperatuur').textContent = pythonData.bodemTemperatuur; // Adjust the property based on your actual Python response
        }
    });

    // Listen for updates to HTML data from the main process
    ipcRenderer.on('update-html-data', (event, data) => {
        // Update the HTML with the received data
        document.getElementById('batteryVoltage').innerText = data.batteryVoltage;
        // Add similar lines for other data fields
    });

    // Trigger an event to request data update
    ipcRenderer.send('request-update-data');

    // Fetch battery data when the page loads
    fetchBatteryData();
});

// Function to draw the chart
function drawLineChart() {
    const canvas = document.getElementById("myCanvas");
    const ctx = canvas.getContext("2d");

    // ... (rest of the function remains unchanged)
}

// Function to fetch battery data from Flask API
function fetchBatteryData() {
    axios.get('http://127.0.0.1:5000/battery_voltage_events') 
        .then(response => {
            const batteryData = response.data;
            updateBatteryData(batteryData);
        })
        .catch(error => {
            console.error('Error fetching battery data:', error);
        });
}


// Function to update HTML content with battery data
function updateBatteryData(batteryData) {
    document.getElementById('deviceNumber').innerText = batteryData.device || 'Niet beschikbaar';
    document.getElementById('voltage').innerText = batteryData.value || 'Niet beschikbaar';
    document.getElementById('time').innerText = batteryData.gateway_receive_time || 'Niet beschikbaar';
    document.getElementById('tevredenheid').innerText = batteryData.timestamp || 'Niet beschikbaar';

}
// Functie om plantgegevens op te halen van Flask API
function fetchPlantData(plantName) {
    axios.get(`http://127.0.0.1:5000/plants?name=${plantName}`) 
        .then(response => {
            const plantData = response.data;
            updatePlantData(plantData);
        })
        .catch(error => {
            console.error('Error fetching plant data:', error);
            // Toon een foutmelding of negeer als de plant niet gevonden is
        });
}

// Functie om HTML-inhoud bij te werken met plantgegevens
function updatePlantData(plantData) {
    // Update de HTML-inhoud met de ontvangen plantgegevens
    document.getElementById('plant_name').innerText = plantData.name || 'Niet beschikbaar';
    document.getElementById('plant_type').innerText = plantData.type || 'Niet beschikbaar';
    document.getElementById('plant_description').innerText = plantData.description || 'Niet beschikbaar';
    document.getElementById('plant_light').innerText = plantData.light || 'Niet beschikbaar';
    document.getElementById('plant_humidity').innerText = plantData.humidity || 'Niet beschikbaar';
}

// Event listener voor het invoerveld waarin de plantnaam wordt ingevoerd
document.getElementById('plant_input').addEventListener('input', function(event) {
    const plantName = event.target.value;
    fetchPlantData(plantName);
});



