import os

# Rootverzeichnis anpassen
root = r"C:\\PTOID"

# PTOID Grundstruktur
folders = [
    "backend/app",
    "backend/models",
    "backend/workflows",
    "backend/plugins",
    "backend/tests",
    "frontend/public",
    "frontend/src/components",
    "frontend/src/api",
    "frontend/electron",
    "mobile-scanner",
    "docs",
    "database",
    "docker",
    ".github/workflows"
]

# Ordner anlegen
for folder in folders:
    path = os.path.join(root, folder)
    os.makedirs(path, exist_ok=True)

# Root-Dateien anlegen
root_files = {
    "LICENSE": "MIT License\n\n(c) 2025 PTOID Projektteam\n...",
    "README.md": "# PTOID - Personal-Transport-of-Important-Datapacks\n\nLokale Dokumentenautomationsplattform\n\n## System: Python + Electron + SQLite + AI\n\n## Lizenz: MIT\n",
    ".gitignore": "__pycache__/\n*.pyc\n*.pyo\n*.pyd\nenv/\nvenv/\nnode_modules/\ndist/\nelectron-builder-cache/\n*.log\n*.db\n.vscode/\n.idea/"
}

for filename, content in root_files.items():
    file_path = os.path.join(root, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ PTOID Grundstruktur erfolgreich erstellt!")