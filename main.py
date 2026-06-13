import os
import shutil

"""
Auto File Organizer
Organizes files in Downloads folder by type.
Built by Shazil waqar using Python.
"""

source = r"C:\Users\YourName\Downloads"

folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "PDFs": [".pdf"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Documents": [".doc", ".docx", ".txt"],
    "Excel": [".xls", ".xlsx", ".csv"],
    "Archives": [".zip", ".rar", ".7z"]
}

files = os.listdir(source)

for file in files:

    file_path = os.path.join(source, file)

    if os.path.isdir(file_path):
        continue

    name ,ext = os.path.splitext(file)

    ext = ext.lower()

    moved = False

    for folder_name, extensions in folders.items():

        if ext in extensions:

            folder_path = os.path.join(source, folder_name)

            os.makedirs(folder_path, exist_ok=True)

            shutil.move(
                file_path,
                os.path.join(folder_path, file),
                )
            moved = True
            print(f"Moved {file} → {folder_name}")
            break
    if not moved:
        print(f"Skipped {file} (unsupported file type)")

        