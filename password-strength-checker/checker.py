import re

print("------ PASSWORD STRENGTH CHECKER ------")

def check_password_strength(password):
    strength = 0

    # Criteria checks
    if len(password) >= 8:
        strength += 1
    if re.search("[a-z]", password):
        strength += 1
    if re.search("[A-Z]", password):
        strength += 1
    if re.search("[0-9]", password):
        strength += 1
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    # Evaluate strength
    if strength == 5:
        return "STRONG password 💪"
    elif strength >= 3:
        return "MEDIUM password 😐"
    else:
        return "WEAK password ⚠️"


while True:
    pwd = input("\nEnter a password to check (or type 'exit'): ")

    if pwd.lower() == "exit":
        print("Goodbye!")
        break

    result = check_password_strength(pwd)
    print("Result:", result)
