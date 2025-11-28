import random
import string

def generate_password(length):
    if length < 4:
        return "Error: Password length must be at least 4 characters."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

print("------ PASSWORD GENERATOR ------")
while True:
    try:
        length = int(input("Enter password length (min 4): "))
        print("Generated Password:", generate_password(length))
    except ValueError:
        print("Please enter a valid number.")

    again = input("Generate another? (y/n): ").lower()
    if again != 'y':
        print("Goodbye!")
        break
