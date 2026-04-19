# 🔐 Password Generator (Flask Web App)

A simple and beginner-friendly **Python Flask web application** that generates secure passwords based on user preferences.

This project is built as a **college-level project** to demonstrate backend integration, form handling, and basic UI design.

---

## 🚀 Features

- Generate random secure passwords
- User-defined password length
- Options to include:
  - Uppercase letters
  - Numbers
  - Symbols
- Ensures at least one character from selected options
- Password strength indicator (Weak / Medium / Strong)
- Copy to clipboard functionality
- Clean and responsive UI

---

## 🛠️ Tech Stack

### 🔹 Backend
- **Python**
- **Flask**
  - Handles routing
  - Processes form data
  - Connects frontend with backend logic

### 🔹 Frontend
- **HTML**
  - Structure of the web page
- **CSS**
  - Styling (gradient background, card layout, responsiveness)
- **JavaScript**
  - Copy-to-clipboard functionality

### 🔹 Python Modules Used
- `random` → for generating random characters  
- `string` → for character sets (letters, digits, symbols)

---

## ⚙️ How It Works

1. User enters password length and selects options
2. Form data is sent to Flask backend
3. Backend:
   - Collects input using `request.form`
   - Builds character pool based on selected options
   - Ensures at least one character from each selected type
   - Generates random password
4. Password is sent back to frontend using Jinja templating
5. Displayed on UI with strength indicator

---

## 📁 Project Structure
password-generator/
│
├── app.py # Flask backend logic
├── templates/
│ └── index.html # UI + Jinja templating
└── static/
└── style.css # Styling
