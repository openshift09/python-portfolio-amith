import os

NOTES_DIR = "notes"

if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)

def show_menu():
    print("\n------ NOTES APP ------")
    print("1. Create Note")
    print("2. List Notes")
    print("3. Read Note")
    print("4. Delete Note")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        title = input("Enter note title: ").strip()
        content = input("Enter note content:\n")

        with open(f"{NOTES_DIR}/{title}.txt", "w") as file:
            file.write(content)

        print("Note created successfully!")

    elif choice == "2":
        notes = os.listdir(NOTES_DIR)
        if not notes:
            print("No notes found.")
        else:
            print("\nYour Notes:")
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note}")

    elif choice == "3":
        note_name = input("Enter note title to read: ").strip() + ".txt"
        filepath = f"{NOTES_DIR}/{note_name}"

        if os.path.exists(filepath):
            print("\n------ NOTE CONTENT ------")
            with open(filepath, "r") as file:
                print(file.read())
        else:
            print("Note not found.")

    elif choice == "4":
        note_name = input("Enter note title to delete: ").strip() + ".txt"
        filepath = f"{NOTES_DIR}/{note_name}"

        if os.path.exists(filepath):
            os.remove(filepath)
            print("Note deleted successfully!")
        else:
            print("Note not found.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
