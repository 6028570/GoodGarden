const { app, BrowserWindow, nativeImage, shell } = require("electron");
// const screen = require("electron").screen;
const path = require("path");

let mainWindow;

function createWindow() 
{
  // const iconPath = path.join(__dirname, "images/logo.png");
  // const icon = nativeImage.createFromPath(iconPath);
  const urlElectron = path.join(__dirname, "src/main.html");

  mainWindow = new BrowserWindow(
  {
    width: 1000,
    height: 650,
    webPreferences: 
    {
      nodeIntegration: true,
    },
    resizable: false,
    frame: true,
    // icon: icon,
    alwaysOnTop: true,
    // backgroundColor: "green"
  });

  // const { width, height } = screen.getPrimaryDisplay().workAreaSize;
  // mainWindow.setPosition(width - 450, height - 500);

  mainWindow.loadURL(urlElectron);

  // mainWindow.on("closed", function () 
  // {
  //   mainWindow = null;
  // });
}

app.on("ready", createWindow);