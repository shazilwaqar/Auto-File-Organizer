# 📂 Auto File Organizer (Python Project)

A simple but powerful Python automation tool that organizes files in your Downloads folder automatically based on file type.

---

## 🚀 Features

- Automatically organizes files by type
- Supports Images, PDFs, Videos, Audio, Documents, Excel, Archives
- Creates folders automatically if they don’t exist
- Skips folders safely
- Lightweight and fast

---

## 🧠 How It Works

The script scans your Downloads folder, checks each file’s extension, and moves it into the correct folder.

Example:
- `.jpg → Images`
- `.pdf → PDFs`
- `.mp4 → Videos`

---

## 📦 Supported File Types

- Images: jpg, jpeg, png, gif  
- PDFs: pdf  
- Videos: mp4, mkv, avi  
- Audio: mp3, wav  
- Documents: doc, docx, txt  
- Excel: xls, xlsx, csv  
- Archives: zip, rar, 7z  

---

## 🛠️ Tech Used

- Python
- os module
- shutil module

---

## ▶️ How to Run

1. Install Python
2. Clone this repo
3. Update path in `main.py`:
   ```python
   source = r"C:\Users\YourName\Downloads"
4. python main.py

## 📸 Screenshots

### Before
![Before](screenshots/before.png)

### After
![After](screenshots/after.png)