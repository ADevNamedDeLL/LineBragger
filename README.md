# LineBragger

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
A colorful, interactive Python terminal app that lets you **brag** about your programming projects!  
Scan a folder, count your lines of code, and get the stats that matter—presented with a vibrant rainbow ASCII UI.

---

## 🎯 Features

- 📂 Folder picker via GUI
- 📊 Smart analysis: 
  - Skips junk files like `node_modules`, `package-lock.json`, `.git`, etc.
  - Only scans actual source files (e.g., `.py`, `.js`, `.cpp`, etc.)
- 📈 Tells you:
  - Number of folders and files
  - Total lines of code
  - Total characters written (your choice)
---

## 🚀 Usage

### 🔧 Requirements

- Python 3.6+
- `colorama`  
- `tkinter` (usually bundled with Python)

Install dependencies:

```bash
pip install colorama
