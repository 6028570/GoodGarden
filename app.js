const { app, BrowserWindow, ipcMain } = require('electron');
const express = require('express');
const bodyParser = require('body-parser');
const { PythonShell } = require('python-shell');
const path = require('path');
const urlElectron = path.join(__dirname, "src/index.html");

// Maak een Express-app
const server = express();
server.use(bodyParser.urlencoded({ extended: true }));

// Definieer een route voor form POST verzoeken
server.post('/submit-form', (req, res) => {
  const { plant_naam, plantensoort } = req.body; // Verkrijg de plant_naam uit het formulier
  const plant_geteelt = req.body.plant_geteelt == 'true' ? 'true' : 'false'; // Zorgt dat de string "true" herkent wordt

  let options = {
    mode: 'text',
    args: [plant_naam, plantensoort, plant_geteelt] // Zet hier een variable bij om de data toe te voegen aan de database
  };

  // Voer Python script uit met de plant_naam als argument
  PythonShell.run('./script/db_connect_form.py', options, (err, results) => {
    if (err) {
      console.error(err);
      res.send('Er is een fout opgetreden');
    } else {
      console.log('Python script uitvoering resultaten:', results);
      res.send('Formulier succesvol verwerkt');
    }
  });
});

// Start de server voor verbinding met de database
const PORT = 3000;
server.listen(PORT, () => {
  console.log(`Server luistert op port ${PORT}`);
});

// Maak de Electron applicatie aan met bijbehorende waardes
function createWindow() {
  const mainWindow = new BrowserWindow({
    width: 1280,
    height: 800,
    frame: false,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  });

  mainWindow.loadURL(urlElectron);
}

app.whenReady().then(createWindow);

// Functionaliteit voor het openen en sluiten van de app
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});


