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
}

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
    if (canvas) 
    {
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
else
{
    console.log("Canvas element does not exist on this page.");
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
                // Converteer datums naar afkortingen van dagen van de week.
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
    // Check if on the specific page where the battery data should be updated
    if (window.location.pathname.endsWith('index.html')) 
    {
        // Update de data voor specifieke apparaten op basis van hun ID.
        const sensor322Element = document.getElementById('deviceNumber-322');
        const sensor256Element = document.getElementById('deviceNumber-256');
        
        if (batteryData[1].device_id === 322 && sensor322Element) 
        {
            sensor322Element.innerHTML = batteryData[1].device_id;
            document.getElementById('voltage-322').innerHTML = batteryData[1].label;
            document.getElementById('time-322').innerHTML = new Date(batteryData[1].last_seen * 1000).toLocaleTimeString();
            document.getElementById('tevredenheid-322').innerHTML = batteryData[1].last_battery_voltage.toFixed(2);
        }
        if (batteryData[0].device_id === 256 && sensor256Element) 
        {
            sensor256Element.innerHTML = batteryData[0].device_id;
            document.getElementById('voltage-256').innerHTML = batteryData[0].label;
            document.getElementById('time-256').innerHTML = new Date(batteryData[0].last_seen * 1000).toLocaleTimeString();
            document.getElementById('tevredenheid-256').innerHTML = batteryData[0].last_battery_voltage.toFixed(2);
        }
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

  function dynamischSensor()
  {
      if (window.location.pathname.endsWith('index.html') || window.location.pathname === '/') 
      {
          const sensor1 = document.getElementById("sensor-1");
          const sensor2 = document.getElementById("sensor-2");
          
          if (sensor1 && sensor2) 
          {
              sensor1.href = `sensor.html?id=${322}`;
              sensor2.href = `sensor.html?id=${256}`;
          }
          else 
          {
              console.log("Elementen 'sensor-1' of 'sensor-2' bestaan niet in de DOM.");
          }
      }
  }
  
  // Aanroepen van de functie
  dynamischSensor();
  

  function closeApplication() {
    if (confirm("Weet je zeker dat je de applicatie wilt sluiten?")) {
        window.close();
    }}

    function fetchPlantenData()
    {
        // Gebruik Axios om een GET-verzoek te versturen naar de planten endpoint.
        axios.get('http://127.0.0.1:5000/planten')
        .then(response => 
        {
            // Verwerk de ontvangen data.
            const plantenData = response.data;
            updatePlantenData(plantenData);
        })
        .catch(error => 
        {
            // Log eventuele fouten tijdens het ophalen.
            console.error('Error fetching planten data:', error);
        });
    }
    
    function getPlantIdFromUrl()
    {
        // Maak een URL-object van de huidige locatie.
        const currentUrl = new URL(window.location.href);
        // Gebruik de URLSearchParams API om de query parameters te verwerken.
        const searchParams = currentUrl.searchParams;
        // Haal de 'id' query parameter op.
        return searchParams.get('id'); // Dit zal een string retourneren of null als het niet bestaat.
    }
    
    function updatePlantenData(plantenData) 
    {
        // Verkrijg de plant ID uit de URL.
        const plantId = parseInt(getPlantIdFromUrl(), 10);
    
        // Vind de plant met die ID in de ontvangen JSON-data.
        const gevondenPlant = plantenData.find(plant => plant.id === plantId);
    
        // Update de titel van de pagina met de naam van de gevonden plant.
        if (gevondenPlant) 
        {
            document.title = gevondenPlant.plant_naam;
            document.querySelector(".plant-titel").textContent = gevondenPlant.plant_naam;
            console.log("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@");
        }
        else 
        {
            console.log(`Geen plant gevonden met ID ${plantId}`);
        }
    }
    
    // Roep fetchPlantenData aan ergens waar het logisch is binnen je applicatielogica, bijvoorbeeld na het laden van de pagina of na een gebruikersactie.
    fetchPlantenData();
    
// Get the battery voltage
const batteryVoltage = parseFloat(document.getElementById('battery-voltage').textContent);
 
// Select the img element
const batteryImage = document.getElementById('battery-image');
 
// Check the battery voltage and decide whether to show the image
if (batteryVoltage < 3.0) {
    // Battery is lower than 3.0 volts, show the empty battery image
    batteryImage.src = '../static/img/warning-logo.png';
} else if (batteryVoltage > 4.2) {
    // Battery is higher than 4.2 volts, do not show the image
    batteryImage.style.display = 'none';
} else {
    // Battery voltage is within the desired range, hide the image
    batteryImage.style.display = 'none';
}