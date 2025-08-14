# 🔐 Secure Encoding & Decoding System

A secure, Python-based **message encoding and decoding** tool with **two interfaces**:

1. **CLI Version** – Lightweight, runs in terminal, no extra libraries required.  
2. **GUI Version** – User-friendly interface built with Tkinter & ttkbootstrap.

---

## 🔹 Features (Both Versions)

- **Dual Interface**
   - CLI version for quick terminal usage
   - GUI version for easy interaction (Windows & Linux support)
     
- **Security Layers:**
   - Caesar cipher (shift cipher)
   - Character rotation
   - Special character token mapping
   - Random prefix/suffix padding

- **Cross-platform:**
   - Works on Windows and Linux

- **No External Dependencies for CLI**
   - GUI uses tkinter + ttkbootstrap for modern UI

- **Icon-based executable build for Windows GUI**
---

## 📂 Project Structure
```
SecureEncodingSystem/
│
├── cli_main.py                   # CLI version
├── assets/
│   └── app.ico                   # Icon for GUI executable (Windows build only)
├── dist/
│   ├── SecureEncoder.exe         # Built executable (Windows GUI version)
│   └── main                      # Built executable (Linux GUI version)
└── README.md                     # This file

```
---

# 🚀 How to Use
1️⃣ **CLI Version**
1.   Clone the repository:
   
   ```bash
   git clone https://github.com/Cryp7icSoul/SecureEncodingSystem.git
   cd SecureEncodingSystem
```
2.   Run the CLI script:

   ```bash
   python cli_main.py
```

3.   Follow on-screen options:
      - 1 → Encode message
      - 2 → Decode message
      - 3 → Exit
---

2️⃣ **GUI Version**

🖥 **Windows**
- Navigate to the dist/ folder and run:
  
```bash
SecureEncoder.exe
 ```
🐧 **Linux**
- Navigate to the dist/ folder and run:

```bash
./main
 ```
(Make sure the file is executable: chmod +x main)

---
# 📸 Screenshots

💻 **CLI Version**

<img width="1907" height="1079" alt="Screenshot 2025-08-14 013459" src="https://github.com/user-attachments/assets/8fe4c6ab-8556-46a2-9ea5-bc2d56f40a34" />

---

🖥 **GUI Version**

<img width="1919" height="1079" alt="Screenshot 2025-08-14 013954" src="https://github.com/user-attachments/assets/eaeb28db-fc30-4175-a6ac-30ee3b1c4d60" />

---
# 🧠 Requirements

**CLI:**
- Python 3.x
- random, string (built-in modules)

---
# ⚖️ License

- This project is open source and free to use.  
- Feel free to modify and share.

---
# 👨‍💻 Author

- Developed by **Muhammad Hamad**  
- 🛡️ Certified Ethical Hacker | 🔍 Penetration Tester  
- 💻 Python & C++ Developer  
- 🌐 [GitHub Profile](https://github.com/Cryp7icSoul/)
- 🔗 [LinkedIn Profile](https://www.linkedin.com/in/cryp7icsoul/)
- 🎯 [TryHackMe Profile](https://tryhackme.com/p/Cryp7icSoul)

