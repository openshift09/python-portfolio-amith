import requests

print("------ CURRENCY CONVERTER ------")

API_URL = "https://api.exchangerate-api.com/v4/latest/"

def convert_currency(base, target, amount):
    try:
        response = requests.get(API_URL + base.upper())
        data = response.json()

        if "rates" not in data:
            print("Invalid Base Currency!")
            return

        rate = data["rates"].get(target.upper())

        if rate is None:
            print("Invalid Target Currency!")
            return

        result = amount * rate
        print(f"\n{amount} {base.upper()} = {result:.2f} {target.upper()}\n")

    except Exception as e:
        print("Error:", str(e))


while True:
    base = input("From Currency (e.g., USD, INR, EUR): ")
    target = input("To Currency (e.g., INR, USD, GBP): ")
    amount = float(input("Amount: "))

    convert_currency(base, target, amount)

    choice = input("Do you want to convert again? (yes/no): ").lower()
    if choice != "yes":
        print("Goodbye!")
        break
