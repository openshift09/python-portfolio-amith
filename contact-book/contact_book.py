import os

FILE_NAME = "contacts.txt"

# Load contacts from file
def load_contacts():
    if not os.path.exists(FILE_NAME):
        open(FILE_NAME, "w").close()
    with open(FILE_NAME, "r") as file:
        contacts = [line.strip().split(",") for line in file.readlines()]
    return contacts

# Save contacts back to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        for name, phone, email in contacts:
            file.write(f"{name},{phone},{email}\n")

def show_menu():
    print("\n------ CONTACT BOOK ------")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

contacts = load_contacts()

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        if not contacts:
            print("No contacts found.")
        else:
            print("\nContacts:")
            for i, (name, phone, email) in enumerate(contacts, start=1):
                print(f"{i}. Name: {name}, Phone: {phone}, Email: {email}")

    elif choice == "2":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        contacts.append([name, phone, email])
        save_contacts(contacts)
        print("Contact added successfully!")

    elif choice == "3":
        search = input("Enter name to search: ").lower()
        found = False
        for name, phone, email in contacts:
            if search in name.lower():
                print(f"Found: {name}, Phone: {phone}, Email: {email}")
                found = True
        if not found:
            print("No matching contacts found.")

    elif choice == "4":
        if not contacts:
            print("No contacts to delete.")
        else:
            for i, (name, phone, email) in enumerate(contacts, start=1):
                print(f"{i}. {name}")
            index = int(input("Enter number to delete: "))
            if 1 <= index <= len(contacts):
                deleted = contacts.pop(index - 1)
                save_contacts(contacts)
                print(f"Deleted contact: {deleted[0]}")
            else:
                print("Invalid choice.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Choose 1-5.")
