import os
import shutil

"""
Auto File Organizer
Organizes files in any folder by type.
Built by Shazil Waqar using Python.
"""

default = os.path.join(os.path.expanduser("~"), "Downloads")

user_input = input(f"Enter folder path to organize (press Enter for {default}): ")
source = user_input.strip() or default

if not os.path.exists(source):
    print(f"❌ Folder not found: {source}")
    exit()

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

    name, ext = os.path.splitext(file)
    ext = ext.lower()
    moved = False

    for folder_name, extensions in folders.items():
        if ext in extensions:
            folder_path = os.path.join(source, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            try:
                shutil.move(file_path, os.path.join(folder_path, file))
                print(f"✅ Moved {file} → {folder_name}")
                moved = True
            except PermissionError:
                print(f"❌ Permission denied: {file} is open or locked")
            except FileExistsError:
                print(f"⚠️ Already exists: {file} skipped")
            except Exception as e:
                print(f"❌ Unexpected error moving {file}: {e}")
            break

    if not moved:
        print(f"⏭️ Skipped {file} (unsupported type)")

        
