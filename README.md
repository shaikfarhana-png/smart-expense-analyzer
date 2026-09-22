# smart-expense-analyzer
A menu-driven Python expense tracking and analysis application.
# 💰 Smart Expense Analyzer

A menu-driven Python application for tracking, managing, and analyzing personal expenses through a simple command-line interface.

The project demonstrates core Python programming concepts such as **lists, dictionaries, loops, conditional statements, user input, and basic data analysis**.

---

## 📌 Features

### 1. Add Expense

Add a new expense by entering:

* Category
* Amount

### 2. View Expenses

View all recorded expenses with their category and amount.

### 3. Search Expense

Search for expenses belonging to a particular category.

The search is case-insensitive, so `Food`, `food`, and `FOOD` are treated as the same category.

### 4. Delete Expense

Delete an expense by selecting its number from the expense list.

### 5. Expense Summary

View an overall summary containing:

* Number of expenses
* Total expenses
* Average expense
* Highest individual expense
* Lowest individual expense

### 6. Category Analysis

Analyze spending by category and identify:

* Total spending per category
* Highest spending category
* Lowest spending category

### 7. Budget Status

Enter a monthly budget and see:

* Total amount spent
* Remaining budget
* Whether the budget is within limit
* Whether the budget has been exceeded

---

## 🛠️ Technologies Used

* **Python 3**
* Lists
* Dictionaries
* Loops
* Conditional Statements
* String Methods
* Basic Input/Output
* Basic Data Analysis

---

## 📂 Project Structure

```text
smart-expense-analyzer/
│
├── expense_analyzer.py    # Main Python application
├── README.md              # Project documentation
├── .gitignore             # Files ignored by Git
│
└── screenshots/
    └── output.png         # Example program output
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/smart-expense-analyzer.git
```

### 2. Open the project

```bash
cd smart-expense-analyzer
```

### 3. Run the application

```bash
python expense_analyzer.py
```

---

## 🖥️ Application Menu

```text
========================================
       SMART EXPENSE ANALYZER
========================================

1. Add Expense
2. View Expenses
3. Search Expense
4. Delete Expense
5. Expense Summary
6. Category Analysis
7. Budget Status
8. Exit

Enter your choice:
```

---

## 📊 Example

Example expenses:

```text
Food       → ₹300
Transport  → ₹150
Food       → ₹450
Shopping   → ₹1000
Food       → ₹250
Transport  → ₹200
```

The application can calculate:

```text
Total Expenses     : ₹2350
Average Expense    : ₹391.67

Highest Expense    : Shopping → ₹1000
Lowest Expense     : Transport → ₹150
```

Category analysis:

```text
Food       : ₹1000
Transport  : ₹350
Shopping   : ₹1000
```

---

## 🧠 Python Concepts Practiced

This project was built using fundamental Python concepts:

```text
Variables
   ↓
User Input
   ↓
Lists
   ↓
Dictionaries
   ↓
Loops
   ↓
Conditional Logic
   ↓
Data Processing
   ↓
Menu-Driven Application
```

The project focuses on understanding the logic behind these concepts rather than relying on advanced libraries.

---

## 🚀 Future Improvements

Planned improvements include:

* [ ] Edit existing expenses
* [ ] Better input validation
* [ ] Save expenses permanently using JSON
* [ ] Load previously saved expenses
* [ ] Refactor code using functions
* [ ] Introduce Object-Oriented Programming
* [ ] Add SQLite database support
* [ ] Add date-based expense tracking
* [ ] Add monthly expense reports
* [ ] Build a web version using Flask/FastAPI
* [ ] Add data visualization

---

## 🎯 Project Goal

The goal of this project is to build a practical Python application while developing strong fundamentals in:

* Data structures
* Problem solving
* Program logic
* Data processing
* User interaction

The project will be progressively upgraded as new Python and backend development concepts are learned.

---

## 👩‍💻 Author

**Farhana**

B.Tech — Computer Science Engineering

---

## 📄 License

This project is open source and available for educational and personal use.
