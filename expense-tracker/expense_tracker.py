import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

# Initialize file with headers if not exists
if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])

def show_menu():
    print("\n------ EXPENSE TRACKER ------")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. Exit")

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Travel, Shopping, etc): ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")
    
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    
    print("Expense added successfully!")

def view_expenses():
    print("\n------ ALL EXPENSES ------")
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def view_total():
    total = 0
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                total += float(row["Amount"])
            except:
                pass
    print(f"\nTotal Expense: ₹{total}")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        view_total()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1-4.")
