# 🧭 Digital Habit Tracker (v1)

A console-based Python project for tracking and reflecting on daily habits — with clean data storage, validations, and timestamped logs.

---

## 🚀 Overview

The **Digital Habit Tracker (DHT)** helps users record their daily habits, durations, and emotions in a structured format.  
Each entry is timestamped and stored in JSON, allowing easy retrieval and reflection later.

It’s designed with:
- Modular and readable structure  
- Strong input validations  
- Persistent local storage  
- Custom exception handling for reliability  

---

## 🧩 Features

- **Add Habit**  
  Record a habit with name, duration, emotion, and timestamp.  

- **View All Habits**  
  Display all stored habits in a clean, formatted table.  

- **View Habits by Date**  
  Filter entries by a specific date (`YYYY-MM-DD`).  

- **Custom Exception Classes**  
  Handles invalid inputs, menu choices, and empty files gracefully.  

- **Persistent Storage**  
  All data is stored automatically in a JSON file (`habits.json`).  

---

## ⚙️ Tech Stack

| Component | Technology |
|------------|-------------|
| Language | Python 3 |
| Storage | JSON |
| Concepts Used | OOP, File Handling, Exception Handling, Input Validation, Modular Functions |

---

## 📂 Project Structure

Digital-Habit-Tracker/<br>
│<br>
├── Data/<br>
│ └── habits.json<br>
│<br>
├── digital_habit_tracker.py<br>
│<br>
└── README.md<br>

---

## ▶️ How to Run

1. Clone the repository:  
   ```bash
   git clone https://github.com/yuvalshahtech/Digital-Habit-Tracker.git
2. Open the project folder:
   ```bash
   cd Digital-Habit-Tracker 
3. Run the script:
   ```bash
    python digital_habit_tracker.py

---
## 🧠 Sample Output
    1. Add a habit
    2. View all habits
    3. View habits by date
    4. Exit
    Enter your choice: 1
    Enter habit: Reading
    Enter duration: 45 minutes
    Enter emotion: Calm
    Habit added successfully!

---

## 🪄 Poster Preview
<img width="1080" height="1080" alt="digital-habit-tracker v1" src="https://github.com/user-attachments/assets/fc803242-d493-468a-ac08-4626fe80d607" />

---

## 👨‍💻 Developer
  Yuval Shah<br>
  GitHub & LinkedIn: [@yuvalshahtech](https://www.linkedin.com/in/yuval-shah-tech/)

---

## 🧭 System Purpose
  This system is built to help users track their habits and reflect on emotions with time-stamped logs.
  It promotes awareness, consistency, and mindful growth — powered by simple, elegant Python logic.
