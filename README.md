# 💸 Python Expense Tracker CLI

A command-line expense tracking application built with Python that helps you log, view, and analyze your daily spending — with persistent JSON storage.

---

## ✨ Features

- **Add expenses** — log amount, category, description, and date with full input validation
- **View all expenses** — display a formatted table of every recorded expense
- **Monthly summary** — filter and total expenses by any specific month and year
- **Persistent storage** — all data saved to `expenses.json` and loaded automatically on startup
- **Input validation** — handles invalid amounts, empty categories, and wrong date formats gracefully

---

## 🖥️ How It Works

```
========================================
EXPENSE TRACKER MENU
========================================
1. Add Expense
2. View All Expenses
3. View Monthly Total
4. Save & Exit
========================================
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x (no external libraries required)

### Run the app

```bash
git clone https://github.com/Anas-Siddiqui-z5941/python-expense-tracker.git
cd python-expense-tracker
python main.py
```

---

## 📁 Project Structure

```
python-expense-tracker/
│
├── main.py            # Entry point — menu loop and user interaction
├── expense_utils.py   # Core functions — add, view, save, load, monthly summary
├── expenses.json      # Auto-generated data file (created on first save)
└── README.md
```

---

## 📊 Sample Output

```
#   Amount     Category        Description                    Date
======================================================================
1   250.00     Food            Lunch at restaurant            2025-06-01
2   1200.00    Transport       Monthly metro pass             2025-06-02
3   499.00     Shopping        Book purchase                  2025-06-05

Total expenses for 6/2025: 1949.00
```

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-000000?style=flat-square&logo=json&logoColor=white)

**Libraries used:** `json` · `os` · `datetime` — all Python built-ins, no pip install needed.

---

## 👤 Author

**Anas Mohiuddin Siddiqui**  
B.Tech CSE @ Integral University | Aspiring ML Engineer  
[LinkedIn](https://www.linkedin.com/in/anas-siddiqui-z5941) • [GitHub](https://github.com/Anas-Siddiqui-z5941)
