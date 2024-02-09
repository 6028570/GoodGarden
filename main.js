const { app, BrowserWindow, nativeImage, shell } = require("electron");
const screen = require("electron").screen;
const path = require("path");

let mainWindow;

function createWindow() {
  const iconPath = path.join(__dirname, "images/logo.png");
  const icon = nativeImage.createFromPath(iconPath);

  mainWindow = new BrowserWindow({
    width: 450,
    height: 500, //moet 500 zijn als frame false is
    webPreferences: {
      nodeIntegration: true,
    },
    resizable: false,
    frame: false,
    icon: icon,
    alwaysOnTop: true,
    backgroundColor: "red"
  });

  const { width, height } = screen.getPrimaryDisplay().workAreaSize;
  mainWindow.setPosition(width - 450, height - 500);

  mainWindow.loadURL("C:/Users/oomen/OneDrive - mboRijnland/Schooljaar 23-24/P3/ALA/GoodGarden/index.html");

  mainWindow.on("closed", function () {
    mainWindow = null;
  });
}

app.on("ready", createWindow);

app.on("window-all-closed", function () {
  if (process.platform !== "darwin") {
    app.quit();
  }
});

app.on("activate", function () {
  if (mainWindow === null) {
    createWindow();
  }
});
