const { ipcRenderer } = require("electron");

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

    // Additional IPC event to update HTML data
    ipcRenderer.on('update-html-data', (event, data) => {
        document.getElementById('battery_data_device_placeholder').innerText = data.battery_data_device;
        document.getElementById('battery_data_voltage_placeholder').innerText = data.battery_data_voltage;
        document.getElementById('battery_data_time_placeholder').innerText = data.battery_data_time;
    });

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
});
