const { app, BrowserWindow } = require('electron');
const path = require('path');
const open = require('open'); // NEU: Browser öffnen

function createWindow () {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    }
  });

  win.loadFile('index.html');

  // 🎵 Easter Egg: Rick Astley spielen 😄
  open('https://www.youtube.com/watch?v=dQw4w9WgXcQ');
}

app.whenReady().then(() => {
  createWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});
