# Secure Encoding & Decoding System

A Python-based secure encoding and decoding system that uses a combination of:

- Caesar cipher (shift cipher)
- Character rotation (shifting first character to the end and vice versa)
- Special character token mapping (for spaces, punctuation, etc.)
- Random padding (prefix and suffix) for added obscurity

This tool allows you to encode a message securely and decode it back to the original text.

---

## Features

- **Encode messages** using a fixed Caesar cipher with character rotation.
- **Decode encoded messages** back to original.
- Handles **special characters and punctuation** by mapping them to unique tokens.
- Adds **random strings as prefix and suffix** to each encoded word to hide the message structure.
- User-friendly command-line interface with options to encode, decode, or exit.
- Input validation and default values for random string length.

---

## How to Use

1. Clone the repository or download the `.py` file.
   
   ```bash
   git clone https://github.com/Cryp7icSoul/SecureEncodingSystem.git
   cd SecureEncodingSystem
   
2. Run the script using:
   ```bash
   python secure_encoding_system.py

3. Follow the on-screen instructions:
    - 1 to Encode
    - 2 to Decode
    - 3 to Exit

4. Enter the random string length when prompted (default = 3).

---

## Example
## Encoding
  Input:
  ```bash
  Hello, World!
  ```
  Output:
  ```bash
  xK9@#Khoor_COMMA__SPC__Zruog_EXCL_$0d%
  ```
## Decoding
  Input:
  ```bash
  xK9@#Khoor_COMMA__SPC__Zruog_EXCL_$0d%
  ``` 
  Output:
  ```bash
  Hello, World!
  ```
---

## Code Structure
- shift_char(c, shift) - Shifts a character by a given amount for encoding.
- unshift_char(c, shift) - Reverses the character shift for decoding.
- random_str(length) - Generates random string padding.
- encoding(length) - Encodes input message with rotation, shift, and padding.
- decoding(length) - Decodes input message by removing padding, reversing token mapping, shift, and rotation.

---

## 🧠 Requirements

- Python 3.x  
- No external libraries required (random and string are built-in)

## ⚖️ License

- This project is open source and free to use.  
- Feel free to modify and share.

## 👨‍💻 Author

- Developed by **Muhammad Hamad**  
- 🛡️ Certified Ethical Hacker | 🔍 Penetration Tester  
- 💻 Python & C++ Developer  
- 🌐 [GitHub Profile](https://github.com/Cryp7icSoul/)
- 🔗 [LinkedIn Profile](https://www.linkedin.com/in/cryp7icsoul/)
- 🎯 [TryHackMe Profile](https://tryhackme.com/p/Cryp7icSoul)
