print("------ PYTHON NOTES APP ------")

def add_note():
    note = input("\nEnter your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note added!")

def view_notes():
    print("\n------ SAVED NOTES ------\n")
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()

        if not notes:
            print("No notes found.")
        else:
            for idx, note in enumerate(notes, 1):
                print(f"{idx}. {note.strip()}")

    except FileNotFoundError:
        print("No notes file found.")

def clear_notes():
    confirm = input("Are you sure you want to delete all notes? (yes/no): ")
    if confirm.lower() == "yes":
        open("notes.txt", "w").close()
        print("All notes cleared!")
    else:
        print("Cancelled.")


# Menu Loop
while True:
    print("""
1. Add Note
2. View Notes
3. Clear All Notes
4. Exit
""")

    choice = input("Choose an option: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        clear_notes()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
