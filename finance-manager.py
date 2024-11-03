import sys
from user_auth import register_user, login_user
from models import add_transaction, set_budget
from database import init_db,get_db_connection

init_db()

def main():
    print("Welcome to Personal Finance Manager")
    user = None
    while not user:
        action = input("Do you want to [register] or [login]? ")
        if action == "register":
            username = input("Enter username: ")
            password = input("Enter password: ")
            register_user(username, password)
        elif action == "login":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = login_user(username, password)
            if not user:
                print("Invalid login credentials.")
    
    user_id = user["id"]
    while True:
        print("\nChoose an option:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Set Budget")
        print("4. View Report")
        print("5. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter income category: ")
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            add_transaction(user_id, "income", category, amount, date)
            print("Income added.")
        elif choice == "2":
            category = input("Enter expense category: ")
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            add_transaction(user_id, "expense", category, amount, date)
            print("Expense added.")
        elif choice == "3":
            category = input("Enter category for budget: ")
            monthly_budget = float(input("Enter monthly budget: "))
            set_budget(user_id, category, monthly_budget)
            print("Budget set.")
        elif choice == "4":
            view_report(user_id)
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Try again.")

def view_report(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) as total_income FROM transactions WHERE user_id = ? AND type = 'income'", (user_id,))
    total_income = cursor.fetchone()["total_income"] or 0.0

    cursor.execute("SELECT SUM(amount) as total_expense FROM transactions WHERE user_id = ? AND type = 'expense'", (user_id,))
    total_expense = cursor.fetchone()["total_expense"] or 0.0

    savings = total_income - total_expense

    print(f"\nReport for User ID: {user_id}")
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expense}")
    print(f"Savings: {savings}")

    conn.close()

if __name__ == "__main__":
    main()
