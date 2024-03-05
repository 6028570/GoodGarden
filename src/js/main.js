const { ipcRenderer } = require("electron");

document.addEventListener('DOMContentLoaded', () => 
{
    ipcRenderer.send('request-update-temp', ['some', 'arguments']);

    ipcRenderer.on('update-temp-result', (event, newTemperature) => {
        if (newTemperature === 'error') {
            console.error('Er is een fout opgetreden bij het ophalen van de nieuwe temperatuur');
        } else {
            document.getElementById('bodem-temperatuur').textContent = newTemperature;
        }
    });

});

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
    
    const yLabels = ["", 20, "", 40, "", 60, "", 80, "", 100]; /*NIET VERANDEREN!!!*/

    const canvas = document.getElementById("myCanvas");
    const ctx = canvas.getContext("2d");

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    const padding = 35; // Increased padding for Y labels
    const graphWidth = canvas.width - padding * 2;
    const graphHeight = canvas.height - padding * 2;

    ctx.beginPath();
    ctx.moveTo(padding, padding);
    ctx.lineTo(padding, canvas.height - padding);
    ctx.lineTo(canvas.width - padding, canvas.height - padding);
    ctx.stroke();

    // Set the color of the line
    ctx.strokeStyle = "rgb(143, 188, 143)";

    const xIncrement = graphWidth / (xLabels.length - 1);
    const yIncrement = graphHeight / (yLabels.length - 1);

    // Plot the data
    ctx.beginPath();
    ctx.moveTo(padding, canvas.height - padding - (data[0] / 100) * graphHeight);

    for (let i = 1; i < data.length; i++)
    {
        const xPos = padding + i * xIncrement;
        const yPos = canvas.height - padding - (data[i] / 100) * graphHeight;
        ctx.lineTo(xPos, yPos);
    }
    ctx.stroke();

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

drawLineChart();