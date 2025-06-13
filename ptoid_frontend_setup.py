import os

# Basisverzeichnis anpassen!
root = r"C:\\PTOID\\frontend"

# Frontend-Unterordner anlegen
folders = [
    "public",
    "src",
    "src/components",
    "src/api",
    "electron"
]

for folder in folders:
    os.makedirs(os.path.join(root, folder), exist_ok=True)

# Beispielhafte Dateien erzeugen
index_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>PTOID</title>
</head>
<body>
  <div id="root"></div>
</body>
</html>
"""

with open(os.path.join(root, "public", "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html.strip())

# Electron Einstiegspunkt
main_js = """
const { app, BrowserWindow } = require('electron');
function createWindow() {
  const win = new BrowserWindow({ width: 1000, height: 800, webPreferences: { nodeIntegration: true } });
  win.loadURL('http://localhost:3000');
}
app.whenReady().then(createWindow);
"""

with open(os.path.join(root, "electron", "main.js"), "w", encoding="utf-8") as f:
    f.write(main_js.strip())

print("✅ PTOID Frontend Grundstruktur erstellt!")
