// Importeer de ipcRenderer-module van Electron voor communicatie tussen processen.
// Dit maakt het mogelijk voor renderer-processen (webpagina's) om berichten te verzenden naar het hoofdproces.
const { ipcRenderer } = require("electron");

// Importeer Axios voor het maken van HTTP-verzoeken
const axios = require('axios');
 
/**
 * Functie om een modaal venster te openen.
 * Deze functie stelt event listeners in voor het openen en sluiten van de modaal.
 */
function openModal()
{
    // Verkrijg de elementen voor de modaal, de open-knop en de sluit-knop op basis van hun ID of klasse.
    const modal = document.getElementById("myModal");
    const button = document.getElementById("modalButton");
    const close = document.getElementsByClassName("close")[0];
 
    // Controleer of de elementen bestaan om fouten te voorkomen.
    if (modal && button) 
    {
        // Toon de modaal wanneer op de knop wordt geklikt.
        button.onclick = function () 
        {
            modal.style.display = "block";
        }
 
        // Sluit de modaal wanneer op het 'sluiten' icoon wordt geklikt.
        close.onclick = function () 
        {
            modal.style.display = "none";
        }
 
        // Sluit de modaal wanneer buiten de modaal wordt geklikt.
        window.onclick = function (event) 
        {
            if (event.target == modal) 
            {
                modal.style.display = "none";
            }
        }
    } 
    else 
    {
        console.error("Modaal elementen niet gevonden");
    }
}

document.addEventListener('DOMContentLoaded', () => 
{
    openModal();
 
    // Roep andere functies hier aan zoals vereist, bijvoorbeeld:
    // fetchWeatherDataAndDrawChart();
 
    // Stuur een bericht naar het hoofdproces om het Python-script uit te voeren.
    ipcRenderer.send('run-python-script', ['some', 'arguments']);
 
    // Luister naar updates van HTML-data vanuit het hoofdproces.
    ipcRenderer.on('update-html-data', (event, data) => 
    {
        // Werk de HTML bij met de ontvangen data.
        document.getElementById('batteryVoltage').innerText = data.batteryVoltage;
        // Voeg vergelijkbare regels toe voor andere data velden.
    });
 
    // Trigger een event om data update aan te vragen.
    ipcRenderer.send('request-update-data');
 
    // Haal batterij data op wanneer de pagina laadt.
    fetchBatteryData();
});
 
/**
 * Functie om een lijngrafiek te tekenen.
 * @param {Array} xLabels Labels voor de x-as.
 * @param {Array} data De data punten voor de grafiek.
 */
function drawLineChart(xLabels, data) 
{
    // Definieer Y labels (niet veranderen volgens commentaar).
    const yLabels = ["", 10, 15, 20, 25, 30, 35, 40];
 
    // Verkrijg het canvas element en de context voor tekenen.
    const canvas = document.getElementById("myCanvas");
    const ctx = canvas.getContext("2d");
 
    // Maak het canvas schoon voor nieuwe tekening.
    ctx.clearRect(0, 0, canvas.width, canvas.height);
 
    // Definieer padding en bereken grafiekafmetingen.
    const padding = 35; // Vergrote padding voor Y labels.
    const graphWidth = canvas.width - padding * 2;
    const graphHeight = canvas.height - padding * 2;
 
    // Teken de as van de grafiek.
    ctx.beginPath();
    ctx.moveTo(padding, padding);
    ctx.lineTo(padding, canvas.height - padding);
    ctx.lineTo(canvas.width - padding, canvas.height - padding);
    ctx.stroke();
 
    // Stel de kleur van de lijn in.
    ctx.strokeStyle = "rgb(143, 188, 143)";
 
    // Bereken incrementen voor het plotten.
    const xIncrement = graphWidth / (xLabels.length - 1);
    const yIncrement = graphHeight / (yLabels.length - 1);
 
    // Plot de data.
    ctx.beginPath();
    ctx.moveTo(padding, canvas.height - padding - (data[0] / 100) * graphHeight);
 
    for (let i = 1; i < data.length; i++) 
    {
        const xPos = padding + i * xIncrement;
        const yPos = canvas.height - padding - (data[i] / 100) * graphHeight;
        ctx.lineTo(xPos, yPos);
    }
    ctx.stroke();
 
    // Teken Y labels.
    ctx.fillStyle = "black";
    ctx.textAlign = "right"; // Tekst naar rechts uitlijnen.
    ctx.textBaseline = "middle"; // Verticaal centreren.
 
    for (let i = 0; i < yLabels.length; i++) 
    {
        if (yLabels[i] !== "") 
        {
            const yPos = canvas.height - padding - i * yIncrement;
            ctx.fillText(yLabels[i], padding - 10, yPos);
        }
    }
 
    // Teken X labels.
    ctx.textAlign = "center"; // Horizontaal centreren voor X labels.
    for (let i = 0; i < xLabels.length; i++) 
    {
        if (xLabels[i] !== "") 
        {
            const xPos = padding + i * xIncrement;
            ctx.fillText(xLabels[i], xPos, canvas.height - padding + 20);
        }
    }
}
 
/**
 * Functie om weergegevens op te halen en een grafiek te tekenen.
 * Deze functie haalt weergegevens op van een lokale server en tekent een lijngrafiek
 * op basis van de verkregen data.
 */
function fetchWeatherDataAndDrawChart() 
{
    // URL van de API waar de weergegevens opgehaald kunnen worden.
    const apiUrl = `http://127.0.0.1:5000/weather`;
 
    // Voer een GET-verzoek uit naar de API.
    fetch(apiUrl)
        .then(response => 
        {
            // Controleer of het verzoek succesvol was.
            if (response.ok) 
            {
                return response.json();
            }
            // Gooi een fout als het verzoek niet succesvol was.
            throw new Error('Network response was not ok.');
        })
        .then(data => 
        {
            // Verkrijg de weersvoorspelling voor de eerste 5 dagen.
            const weatherForecast = data.weather_forecast.slice(0, 5);
            // Converteer datums naar dagen van de week.
            const dates = weatherForecast.map(day => convertDateToDayOfWeek(day.dag));
            // Verkrijg de maximale temperaturen.
            const temperatures = weatherForecast.map(day => day.max_temp);
 
            // Teken de lijngrafiek met de verkregen data.
            drawLineChart(dates, temperatures);
        })
        .catch(error => 
        {
            // Log eventuele fouten tijdens het ophalen.
            console.error('There was a problem with the fetch operation:', error);
        });
}
 
/**
 * Functie om een datum (bijv. "07-02") om te zetten naar de dag van de week (bijv. "zo", "ma", etc.).
 * @param {string} dateString - De datum als string in het formaat "dd-mm".
 * @returns {string} De afkorting van de dag van de week.
 */
function convertDateToDayOfWeek(dateString) 
{
    // Split de datum in dag en maand, en zet deze om naar nummers.
    const [day, month] = dateString.split('-').map(Number);
    // Maak een nieuwe datumobject (jaar is willekeurig omdat we alleen maand en dag nodig hebben).
    const date = new Date(2024, month - 1, day);
    // Verkrijg de dag van de week en zet deze om naar een afkorting.
    const dayOfWeek = ['zo', 'ma', 'di', 'wo', 'do', 'vr', 'za'][date.getDay()];
    return dayOfWeek;
}
 
/**
 * Functie om batterijdata op te halen wanneer de pagina laadt.
 * Deze functie haalt data op met Axios en verwerkt deze vervolgens.
 */
function fetchBatteryData() 
{
    // Voer een GET-verzoek uit naar de server om batterijdata op te halen.
    axios.get('http://127.0.0.1:5000')
        .then(response => 
        {
            // Verwerk de ontvangen data.
            const batteryData = response.data;
            updateBatteryData(batteryData);
        })
        .catch(error => 
        {
            // Log eventuele fouten tijdens het ophalen.
            console.error('Error fetching battery data:', error);
        });
}
 
/**
 * Functie om batterijdata op de pagina bij te werken.
 * Deze functie update de HTML met de ontvangen batterijdata.
 * @param {Array} batteryData - De ontvangen batterijdata.
 */
function updateBatteryData(batteryData) 
{
    // Update de data voor specifieke apparaten op basis van hun ID.
    if (batteryData[1].device_id == 322) 
    {
        document.getElementById('deviceNumber-322').innerHTML = batteryData[1].device_id;
        document.getElementById('voltage-322').innerHTML = batteryData[1].label;
        document.getElementById('time-322').innerHTML = new Date(batteryData[0].last_seen).toLocaleTimeString();
        document.getElementById('tevredenheid-322').innerHTML = batteryData[1].last_battery_voltage;
    }
    if (batteryData[0].device_id == 256) 
    {
        document.getElementById('deviceNumber-256').innerHTML = batteryData[0].device_id;
        document.getElementById('voltage-256').innerHTML = batteryData[0].label;
        document.getElementById('time-256').innerHTML = new Date(batteryData[0].last_seen).toLocaleTimeString();
        document.getElementById('tevredenheid-256').innerHTML = batteryData[0].last_battery_voltage;
    }
}
 
// Definieer de API-sleutel en de stad waarvoor we de weergegevens willen ophalen.
const apiKey = "9516081f15727d063c9e2f08454a2fe9";
const city = "Leiden";
 
// Construeer de URL voor de API-aanroep. In dit geval is het een lokale server.
const apiUrl = `http://127.0.0.1:5000/weather`;
 
// Voer een GET-verzoek uit naar de API om de weergegevens op te halen.
fetch(apiUrl)
  .then(response => 
  {
    // Controleer of de respons van de server in orde is (status code 200).
    if (response.ok) 
    {
      // Zo ja, parse de JSON uit de respons.
      return response.json();
    }
    // Zo niet, gooi een fout.
    throw new Error('Network response was not ok.');
  })
  .then(data => 
  {
    // Log de ontvangen data naar de console voor debugging.
    console.log(data);
 
    // Extraheren van de weersvoorspelling voor de eerste vijf dagen.
    const weatherForecast = data.weather_forecast.slice(0, 5);
    // Haal de dagen op waarvoor de voorspelling geldt.
    const dates = weatherForecast.map(day => day.dag);
    // Haal de maximale temperaturen op voor deze dagen.
    const temperatures = weatherForecast.map(day => day.max_temp);
 
    // Update de grafiek met de nieuwe data.
    drawLineChart(dates, temperatures);
  })
  .catch(error => 
  {
    // Log eventuele fouten tijdens het ophalen van de data.
    console.error('There was a problem with the fetch operation:', error);
  });