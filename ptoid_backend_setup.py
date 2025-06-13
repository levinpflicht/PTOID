import os

# Basisverzeichnis anpassen!
root = r"C:\\PTOID\\backend"

# Backend-Unterordner anlegen
folders = ["app", "models", "workflows", "plugins", "tests"]
for folder in folders:
    os.makedirs(os.path.join(root, folder), exist_ok=True)

# requirements.txt erzeugen
requirements = """
Flask==3.0.0
pytesseract==0.3.13
vosk==0.3.50
openai-whisper==20230918
invoice2data==0.4.5
pandas==2.3.0
language-tool-python==2.9.4
pyspellchecker==0.8.3
PyPDF2==3.0.1
python-docx==1.1.0
sqlcipher3==0.4.0
"""

with open(os.path.join(root, "requirements.txt"), "w", encoding="utf-8") as f:
    f.write(requirements.strip())

# Beispiel-App-Dateien erzeugen
main_py = """
from flask import Flask
from app import ocr_module, stt_module, parsing_module

app = Flask(__name__)

@app.route('/')
def home():
    return "PTOID Backend API is running."

if __name__ == '__main__':
    app.run(port=5000)
"""

with open(os.path.join(root, "app", "main.py"), "w", encoding="utf-8") as f:
    f.write(main_py.strip())

# Dummy-Module für Start erzeugen
module_files = [
    "ocr_module.py",
    "stt_module.py",
    "parsing_module.py",
    "correction_module.py",
    "export_module.py"
]

for module in module_files:
    path = os.path.join(root, "app", module)
    with open(path, "w", encoding="utf-8") as f:
        f.write("# TODO: Implement " + module)

print("✅ PTOID Backend Grundstruktur fertig installiert!")