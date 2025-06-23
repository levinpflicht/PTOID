from flask import Flask
from . import ocr_module, stt_module, parsing_module

app = Flask(__name__)

@app.route('/')
def home():
    return "PTOID Backend API is running."

if __name__ == '__main__':
    app.run(port=5000)
