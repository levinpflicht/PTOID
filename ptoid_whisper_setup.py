import os

root = r"C:\\PTOID\\backend_whisper"

os.makedirs(root, exist_ok=True)

requirements = """
openai-whisper==20230918
torch==2.2.2
tqdm
ffmpeg-python
"""

with open(os.path.join(root, "requirements.txt"), "w", encoding="utf-8") as f:
    f.write(requirements.strip())

main_py = """
# Whisper API Einstiegspunkt
print("✅ PTOID Whisper Environment bereit!")
"""

with open(os.path.join(root, "main.py"), "w", encoding="utf-8") as f:
    f.write(main_py.strip())

print("✅ PTOID Whisper Struktur erfolgreich erzeugt!")
