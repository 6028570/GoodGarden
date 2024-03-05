const { app, BrowserWindow,ipcMain } = require('electron'); /* TYPE IN TERMINAL: "npm install electron" */
const express = require('express');  /* TYPE IN TERMINAL: "npm install express" */
const bodyParser = require('body-parser');  /* TYPE IN TERMINAL: "npm install body-parser" */
const { PythonShell } = require('python-shell');  /* TYPE IN TERMINAL: "npm install python-shell" */
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
    args: [plant_naam, plantensoort, plant_geteelt], // Zet hier een variable bij om de data toe te voegen aan de databas
  };

/*Om python te gebruiken*/
// ipcMain.on('request-update-temp', (event, args) => {
//   let options = {
//       mode: 'text',
//       scriptPath: 'path/to/your/python/script',
//       args: args
//   };

//   PythonShell.run('calculate.py', options, (err, results) => {
//       if (err) {
//           console.error('Error running python script', err);
//           event.reply('update-temp-result', 'error');
//       } else {
//           console.log('Python script results:', results);
//           event.reply('update-temp-result', results[0]); // Verstuur het resultaat terug naar de renderer proces
//       }
//   });
// });

// En dan in je renderer proces, stuur je een bericht om de update te verzoeken
ipcRenderer.send('request-update-temp', [/* hier kunnen argumenten komen die je Python script nodig heeft */]);

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

  /*Is om het Python script te kunnen gebruiken*/
  ipcMain.on('run-python-script', (event, args) => {
    let options = {
        mode: 'text',
        args: args
    };

    PythonShell.run('../src/py/calculate.py', options, (err, results) => {
        if (err) 
        {
            console.error('Error running python script', err);
            event.reply('python-script-response', 'error');
        } 
        else 
        {
            console.log('Python script results:', results);
            event.reply('python-script-response', results);
        }
    });
});
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