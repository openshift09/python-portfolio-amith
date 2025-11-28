import csv
from datetime import datetime

print("------ EXPENSE TRACKER ------")

CSV_FILE = "expenses.csv"

# Ensure CSV has headers
def init_file():
    try:
        with open(CSV_FILE, "r") as file:
            pass
    except:
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])

def add_expense():
    category = input("Enter category (Food/Travel/Bills/Other): ")
    desc = input("Enter description: ")
    amount = float(input("Enter amount: "))

    date = datetime.now().strftime("%Y-%m-%d")

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, desc, amount])

    print("Expense added successfully!")

def view_expenses():
    print("\n------ ALL EXPENSES ------\n")
    total = 0

    with open(CSV_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header

        for row in reader:
            print(row)
            total += float(row[3])

    print(f"\nTotal Spending: ₹{total}\n")

def menu():
    while True:
        print("""
1. Add Expense
2. View Expenses
3. Exit
""")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

init_file()
menu()
