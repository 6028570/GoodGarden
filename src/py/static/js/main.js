const { ipcRenderer } = require("electron");
const axios = require('axios');

document.addEventListener('DOMContentLoaded', () => {
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

    // Function to open the modal
    function openModal() {
        const modal = document.getElementById("myModal");
        const button = document.getElementById("modalButton");
        const close = document.getElementsByClassName("close")[0];

        // Check if elements are found before attaching events
        if (modal && button && close) {
            // Show the modal when the button is clicked
            button.onclick = function () {
                modal.style.display = "block";
            }

            // Close the modal when the 'close' icon is clicked
            close.onclick = function () {
                modal.style.display = "none";
            }

            // Close the modal when clicked outside the modal
            window.onclick = function (event) {
                if (event.target == modal) {
                    modal.style.display = "none";
                }
            }
        }
    }

    // Call the function to open the modal
    openModal();

    /**
     * --- Function to draw the chart. The important arrays are "data" & "xLabels".
     */
    function drawLineChart() {
        const canvas = document.getElementById("myCanvas");
        const ctx = canvas.getContext("2d");

        // ... (rest of the function remains unchanged)
    }

    // Call the function to draw the line chart
    drawLineChart();

    // Function to fetch battery data from Flask API
    function fetchBatteryData() {
        axios.get('http://127.0.0.1:5000')
            .then(response => {
                const batteryData = response.data;
                updateBatteryData(batteryData);
            })
            .catch(error => {
                console.error('Error fetching battery data:', error);
            });
    }

// Function to update HTML content with battery data
function updateBatteryData(batteryData){
    document.getElementById('deviceNumber').innerText = batteryData.device;
    document.getElementById('voltage').innerText = batteryData.value;
    document.getElementById('time').innerText = batteryData.gateway_receive_time;
    document.getElementById('tevredenheid').innerText = batteryData.timestamp;

    // Voeg andere eigenschappen toe zoals nodig
}



    // Fetch battery data when the page loads
    fetchBatteryData();
});
