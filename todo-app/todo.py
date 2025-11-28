import os

FILE_NAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(FILE_NAME):
        open(FILE_NAME, 'w').close()
    with open(FILE_NAME, "r") as file:
        tasks = [task.strip() for task in file.readlines()]
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_menu():
    print("\n-------- TO-DO LIST APP --------")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

tasks = load_tasks()

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print("\nYour Tasks:")
        if not tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        new_task = input("Enter new task: ")
        tasks.append(new_task)
        save_tasks(tasks)
        print("Task added.")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
            continue
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"Deleted: {removed}")
        else:
            print("Invalid number.")

    elif choice == "4":
        print("Exiting To-Do List App. Goodbye!")
        break

    else:
        print("Invalid choice. Please choose 1-4.")
