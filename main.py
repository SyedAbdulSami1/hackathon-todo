from todo import TodoManager

def print_menu():
    """Prints the main menu options to the console."""
    print("\n--- To-do List Menu ---")
    print("1. Add a new task")
    print("2. List all tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Exit")
    print("-----------------------")

def main():
    """Main function to run the to-do list application."""
    todo_manager = TodoManager()

    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter the task title: ")
            if not title.strip():
                print("Error: Title cannot be empty.")
                continue
            description = input("Enter the task description: ")
            task = todo_manager.add_task(title, description)
            # Placeholder for T-006
            print(f"Success: Task '{task.title}' added.")

        elif choice == '2':
            tasks = todo_manager.list_tasks()
            if not tasks:
                print("No tasks in the list.")
            else:
                print("\n--- Your To-Do List ---")
                for task in tasks:
                    status = "Complete" if task.completed else "Incomplete"
                    print(f"ID: {task.id}")
                    print(f"  Title: {task.title}")
                    print(f"  Description: {task.description}")
                    print(f"  Status: {status}")
                    print("-" * 20)

        elif choice == '3':
            # To be implemented in a future feature
            print("Mark task functionality will be implemented soon.")
            pass
        elif choice == '4':
            # To be implemented in a future feature
            print("Delete task functionality will be implemented soon.")
            pass
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
