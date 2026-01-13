import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

# Create CSV file if not exists
def initialize_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Type", "Amount"])
    except FileExistsError:
        pass

# Add new income/expense entry
def add_entry():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, Salary, etc.): ")
    entry_type = input("Enter type (Income/Expense): ").capitalize()
    amount = float(input("Enter amount: "))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, entry_type, amount])

    print("Entry added successfully!\n")

# View monthly summary
def view_summary():
    month = input("Enter month (YYYY-MM): ")

    total_income = 0
    total_expense = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Date"].startswith(month):
                amount = float(row["Amount"])
                if row["Type"] == "Income":
                    total_income += amount
                else:
                    total_expense += amount

    print("\n----- Monthly Summary -----")
    print("Total Income :", total_income)
    print("Total Expense:", total_expense)
    print("Savings      :", total_income - total_expense)
    print("---------------------------\n")

# Main menu
def main():
    initialize_file()
    
    while True:
        print("===== Expense Tracker CLI =====")
        print("1. Add Entry")
        print("2. View Monthly Summary")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Try again.\n")

# Run program
main()