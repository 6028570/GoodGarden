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
server.post('/submit-form', (req, res) => {
  const { plant_naam, plantensoort } = req.body;
  const plant_geteelt = req.body.plant_geteelt == 'true' ? 'true' : 'false';

  let options = {
    mode: 'text',
    args: [plant_naam, plantensoort, plant_geteelt],
  };

  // The following line was causing issues and has been commented out
  // ipcRenderer.send('request-update-temp', [/* arguments for Python script */]);
});

// Start the server for connecting to the database
const PORT = 3000;
server.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT}`);
});

let mainWindow; // Variable to store the reference to the main window

// Create the Electron application with associated values
function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1280,
    height: 800,
    frame: false,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
      enableRemoteModule: true,
      webSecurity: true,
    }
  });

  mainWindow.loadFile(path.join(__dirname, 'src', 'py', 'templates', 'index.html'));

  // Enable Python script execution
  ipcMain.on('run-python-script', (event, args) => {
    let options = {
      mode: 'text',
      args: args,
    };

    PythonShell.run('../src/py/calculate.py', options, (err, results) => {
      if (err) {
        console.error('Error running python script', err);
        event.reply('python-script-response', 'error');
      } else {
        console.log('Python script results:', results);

        // Send the Python data to the renderer process
        mainWindow.webContents.send('python-script-response', JSON.parse(results[0]));
      }
    });
  });

  // IPC event for updating HTML with data received from Python
  ipcMain.on('update-html-data', (event, data) => {
    mainWindow.webContents.send('update-html-data', data);
  });
}

// Start the Electron app
app.whenReady().then(() => {
  createWindow();

  // Execute Python script when the app is ready
  const options = {
    mode: 'text',
    scriptPath: path.join(__dirname, 'src', 'py'),
    args: [/* arguments for the Python script */]
  };

  PythonShell.run('calculate.py', options, (err, results) => {
    if (err) {
      console.error('Error running python script', err);
      mainWindow.webContents.send('python-script-response', 'error');
    } else {
      console.log('Python script results:', results);

      // Send the Python data to the renderer process
      mainWindow.webContents.send('python-script-response', JSON.parse(results[0]));
    }
  });
});

// IPC event for requesting data update
ipcMain.on('request-update-data', (event, args) => {
  // Implement logic to get data from the database if needed
  const databaseData = { timestamp: "2022-01-01", gateway_receive_time: "2022-01-01", device: "Device1", value: 50 };

  // Send updated data to the renderer process
  event.reply('update-data-result', { databaseData });
});

// Functionalities for opening and closing the app
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
