const { app, BrowserWindow, ipcMain } = require('electron');
const express = require('express');
const bodyParser = require('body-parser');
const { PythonShell } = require('python-shell');
const path = require('path');

const urlElectron = path.join(__dirname, "src/index.html");

// Create an Express app
const server = express();
server.use(bodyParser.urlencoded({ extended: true }));

// Define a route for form POST requests
server.post('/submit-form', (req, res) => 
{
  const { plant_naam, plantensoort } = req.body;
  const plant_geteelt = req.body.plant_geteelt == 'true' ? 'true' : 'false';

  let options = 
  {
    mode: 'text',
    args: [plant_naam, plantensoort, plant_geteelt]
  };

  // Execute Python script with plant name as an argument
  PythonShell.run('src/py/script/db_connect_form.py', options, (err, results) => 
  {
    if (err) 
    {
      console.error(err);
      res.send('Er is een fout opgetreden');
    } 
    else 
    {
      console.log('Python script uitvoering resultaten:', results);
      res.send('Formulier succesvol verwerkt');
    }
  });
});

// Start the server
const PORT = 3000;
server.listen(PORT, () => 
{
  console.log(`Server is listening on port ${PORT}`);
});

let mainWindow;

// Create the Electron application window
function createWindow() 
{
  mainWindow = new BrowserWindow(
  {
    width: 1280,
    height: 800,
    frame: false,
    webPreferences: 
    {
      nodeIntegration: true,
      contextIsolation: false,
      enableRemoteModule: true,
      webSecurity: true,
    }
  });

  mainWindow.loadFile(path.join(__dirname, 'src', 'py', 'templates', 'index.html'));

  // IPC event listeners for running Python scripts and updating HTML data
  setupIpcMainListeners();
}

// Start the Electron app
app.whenReady().then(createWindow);

// Close the app when all windows are closed, except on macOS
app.on('window-all-closed', () => 
{
  if (process.platform !== 'darwin') 
  {
    app.quit();
  }
});

// Re-create a window in the app when the dock icon is clicked and there are no other windows open.
app.on('activate', () => 
{
  if (BrowserWindow.getAllWindows().length === 0) 
  {
    createWindow();
  }
});

function setupIpcMainListeners() 
{
  ipcMain.on('run-python-script', (event, args) => 
  {
    let options = 
    {
      mode: 'text',
      args: args,
    };

    // The actual script path and event replies should be tailored to your application's needs
  });

  ipcMain.on('request-update-data', (event, args) => 
  {
    const databaseData = { timestamp: "2022-01-01", gateway_receive_time: "2022-01-01", device: "Device1", value: 50 };
    event.reply('update-data-result', { databaseData });
  });

  ipcMain.on('update-html-data', (event, data) => 
  {
    mainWindow.webContents.send('update-html-data', data);
  });
}