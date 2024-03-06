const { ipcRenderer } = require("electron");

document.addEventListener('DOMContentLoaded', () => 
{
    // Stuur een bericht naar de main process om het Python script uit te voeren
// In je renderer.js (geladen met defer in je HTML)
    ipcRenderer.send('request-update-temp', ['some', 'arguments']);

    ipcRenderer.on('update-temp-result', (event, newTemperature) => {
        if (newTemperature === 'error') {
            console.error('Er is een fout opgetreden bij het ophalen van de nieuwe temperatuur');
        } else {
            document.getElementById('bodem-temperatuur').textContent = newTemperature;
        }
    });

});

// function dataTablePython()
// {
//     document.getElementById("")
// }

function openModal()
{
    const modal = document.getElementById("myModal");
    const button = document.getElementById("modalButton");
    const close = document.getElementsByClassName("close")[0];

    // Toon de modal wanneer op de knop wordt geklikt
    button.onclick = function()
    {
        modal.style.display = "block";
    }

    // Sluit de modal wanneer op het 'sluiten' icoon wordt geklikt
    close.onclick = function() 
    {
        modal.style.display = "none";
    }

    // Sluit de modal wanneer buiten de modal wordt geklikt
    window.onclick = function(event) 
    {
        if (event.target == modal) 
        {
            modal.style.display = "none";
        }
    }
}

/**
 * --- Functie om de grafiek te tekenen. Enigste belangrijke is de eerste 2 "const" arrays "data" & "xLabels".
 */
function drawLineChart()
{
    /*Dit is de data die getoond wordt als "punt" op de grafiek. 20 = y20 / x20, 50 = y50 / x50 enzovoort... De array "data" & "xLabels" moeten beide evenveel array items hebben!!*/
    const data = [20, 50, 60, 45, 50, 100, 70, 60, 65, 0, 85, 0];
    const xLabels = ["", "", "", "", "", 6, "", "", "", "", "", 12];
    
    // Define Y-axis labels here. The number of labels should match your scale.
    const yLabels = ["", 20, "", 40, "", 60, "", 80, "", 100]; /*NIET VERANDEREN!!!*/

    const canvas = document.getElementById("myCanvas");
    const ctx = canvas.getContext("2d");

    ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas

    const padding = 35; // Increased padding for Y labels
    const graphWidth = canvas.width - padding * 2;
    const graphHeight = canvas.height - padding * 2;

    // Draw the axes
    ctx.beginPath();
    ctx.moveTo(padding, padding);
    ctx.lineTo(padding, canvas.height - padding);
    ctx.lineTo(canvas.width - padding, canvas.height - padding);
    ctx.stroke();

    // Set the color of the line
    ctx.strokeStyle = "#008000"; // This sets the line color to green

    const xIncrement = graphWidth / (xLabels.length - 1);
    const yIncrement = graphHeight / (yLabels.length - 1); // Assuming you have labels for each increment

    // Plot the data
    ctx.beginPath();
    ctx.moveTo(padding, canvas.height - padding - (data[0] / 100) * graphHeight);

    for (let i = 1; i < data.length; i++)
    {
        const xPos = padding + i * xIncrement;
        const yPos = canvas.height - padding - (data[i] / 100) * graphHeight;
        ctx.lineTo(xPos, yPos);
    }
    ctx.stroke(); // Apply the stroke to the line

    // Draw Y labels
    ctx.fillStyle = "black";
    ctx.textAlign = "right"; // Align text to the right
    ctx.textBaseline = "middle"; // Center vertically

    for (let i = 0; i < yLabels.length; i++)
    {
        if (yLabels[i] !== "")
        {
            const yPos = canvas.height - padding - i * yIncrement;
            ctx.fillText(yLabels[i], padding - 10, yPos);
        }
    }

    // Draw X labels
    ctx.textAlign = "center"; // Center horizontally for X labels
    for (let i = 0; i < xLabels.length; i++)
    {
        if (xLabels[i] !== "")
        {
            const xPos = padding + i * xIncrement;
            ctx.fillText(xLabels[i], xPos, canvas.height - padding + 20);
        }
    }
}

  
document.addEventListener('DOMContentLoaded', function() {
    var battery_data = {
        device: "{{ battery_data[2] }}",
        batteryVoltage: "{{ battery_data[3] }}",
        time: "{{ battery_data[1] }}"
    };

    // Update HTML elements using dynamically generated IDs
    document.getElementById('battery_data_device').innerText = battery_data.device;
    document.getElementById('battery_data_voltage').innerText = battery_data.batteryVoltage;
    document.getElementById('battery_data_time').innerText = battery_data.time;
    // Add other updates as needed
});


    
  
drawLineChart();