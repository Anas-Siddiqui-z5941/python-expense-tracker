from datetime import datetime
import os
import json

def add_expense(expenses):
    """Add an expense to the expenses.json file."""
    
    try:
        while True:
            amount = float(input("Enter the amount spent: "))
            if amount <= 0:
                print("Enter the valid amount.")
                continue
            break
    except ValueError:
        print("Invalid input. Please enter a numeric value for the amount.")

    category = input("Enter the category of the expense: ").strip()
    if not category:
        category = input("Category cannot be empty. Please enter the category of the expense: ").strip()
    
    description = input("Enter a description for the expense (optional): ")

    while True:    
        date = input("Enter the date of the expense (YYYY-MM-DD): ")
        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

    expense_data = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    expenses.append(expense_data)

    print("\nExpense added successfully!")

def view_expenses(expenses):
    """View all expenses."""
    if not expenses:
        print("\nNo expenses found.")
    else:
        print(f"{'#':<3} {'Amount':<10} {'Category':<15} {'Description':<30} {'Date':<12}")
        print("=" * 70)
        for idx, expense in enumerate(expenses, start=1):
            print(f"{idx:<3} {expense['amount']:<10.2f} {expense['category']:<15} {expense['description']:<30} {expense['date']:<12}")

def save_expenses(expenses,):
    """Save expenses to the file."""
    try:    
        with open ("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)
        print("\nExpenses saved successfully!")
    except IOError:
        print("An error occurred while saving expenses. Please try again.")

def load_expenses():
    """Load expenses from the file."""
    if os.path.exists("expenses.json"):
        try:
            with open("expenses.json", "r") as file:
                expenses = json.load(file)
            print("\nExpenses loaded successfully!")
            return expenses
        except (IOError, json.JSONDecodeError):
            print("An error occurred while loading expenses. Starting with an empty list.")
            return []
    else:
        return []
    
def total_monthly_expenses(expenses):
    """Calculate and display total expenses for the specific month."""
    while True:
            try:
                month = int(input("Enter month (1-12): "))
                if 1 <= month <= 12:
                    break
                print("Month must be between 1 and 12.")
            except ValueError:
                print("Please enter a valid number.")
    
    while True:
        try:
            year = int(input("Enter year (e.g., 2024): "))
            if 1000 <= year <= 9999:
                break
            print("Please enter a valid year.")
        except ValueError:
            print("Please enter a valid number.")
    
    total = 0
    Monthly_expenses = []
    for expense in expenses:
        expense_date = datetime.strptime(expense["date"], "%Y-%m-%d")
        if expense_date.month == int(month) and expense_date.year == int(year):
            total += expense["amount"]
            Monthly_expenses.append(expense)

    print(f"\nTotal expenses for {month}/{year}: {total:.2f}")

    if Monthly_expenses:
        print(f"\n{'#':<3} {'Amount':<10} {'Category':<15} {'Description':<30} {'Date':<12}")
        for idx, expense in enumerate(Monthly_expenses, start=1):
            print(f"{idx:<3} {expense['amount']:<10.2f} {expense['category']:<15} {expense['description']:<30} {expense['date']:<12}")




       
    


    



    