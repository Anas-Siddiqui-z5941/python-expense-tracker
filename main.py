import expense_utils as eu

def main():
    expenses = eu.load_expenses()
    
    while True:
        print("\n" + "="*40)
        print("EXPENSE TRACKER MENU")
        print("="*40)
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Monthly Total")
        print("4. Save & Exit")
        print("="*40)
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            eu.add_expense(expenses)
        elif choice == '2':
            eu.view_expenses(expenses)
        elif choice == '3':
            eu.total_monthly_expenses(expenses)
        elif choice == '4':
            eu.save_expenses(expenses)
            print("Thank you for using Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()