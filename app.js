function closeWindow() {
  window.close();
}

document.getElementById("close").addEventListener("click", closeWindow);

function minimizeWindow() {
  remote.getCurrentWindow().minimize();
}
// werkt niet!!!
document.getElementById("minimize").addEventListener("click", minimizeWindow);
