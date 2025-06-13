name: PTOID Build Pipeline

on:
  push:
    branches: [ main, dev ]
  pull_request:
    branches: [ main, dev ]

jobs:
  build:
    runs-on: windows-latest

    steps:
    - name: Checkout Repository
      uses: actions/checkout@v3

    - name: Setup Python 3.13 for Backend
      uses: actions/setup-python@v4
      with:
        python-version: '3.13'

    - name: Setup Python 3.11 for Whisper
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
        architecture: 'x64'

    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'

    - name: Install Node Dependencies
      run: |
        cd frontend
        npm install

    - name: Install Python 3.13 Backend Dependencies
      run: |
        cd backend
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Install Python 3.11 Whisper Dependencies
      run: |
        cd backend_whisper
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run Backend Tests
      run: |
        cd backend/tests
        python -m unittest discover
