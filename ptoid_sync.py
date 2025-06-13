import os
import shutil

# Quellverzeichnisse hier eintragen, wo aktuell deine einzelnen Module noch liegen:
source_backend = r"C:\(DEIN AKTUELLER BACKEND PFAD)"
source_frontend = r"C:\(DEIN AKTUELLER FRONTEND PFAD)"
source_backend_whisper = r"C:\(DEIN AKTUELLER WHISPER PFAD)"
source_github = r"C:\(DEIN AKTUELLER GITHUB WORKFLOW PFAD)"

# Zielverzeichnis für dein PTOID Git Repository:
target_root = r"C:\PTOID"

# Ordnerstruktur anlegen
folders = ["backend", "frontend", "backend_whisper", ".github/workflows"]

for folder in folders:
    os.makedirs(os.path.join(target_root, folder), exist_ok=True)

# Dateien kopieren
shutil.copytree(source_backend, os.path.join(target_root, "backend"), dirs_exist_ok=True)
shutil.copytree(source_frontend, os.path.join(target_root, "frontend"), dirs_exist_ok=True)
shutil.copytree(source_backend_whisper, os.path.join(target_root, "backend_whisper"), dirs_exist_ok=True)
shutil.copytree(source_github, os.path.join(target_root, ".github", "workflows"), dirs_exist_ok=True)

print("✅ PTOID Dateien vollständig synchronisiert.")
