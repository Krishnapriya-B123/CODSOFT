tasks = []

def display_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i}. {task['task']} - {status}")

while True:
    print("\n===== TO-DO LIST APPLICATION =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task_name = input("Enter task: ")
        tasks.append({"task": task_name, "completed": False})
        print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        display_tasks()

    # Update Task
    elif choice == "3":
        display_tasks()
        num = int(input("Enter task number to update: "))
        if 1 <= num <= len(tasks):
            new_task = input("Enter updated task: ")
            tasks[num - 1]["task"] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

    # Mark Task as Completed
    elif choice == "4":
        display_tasks()
        num = int(input("Enter task number to mark completed: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    # Delete Task
    elif choice == "5":
        display_tasks()
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")

    # Exit
    elif choice == "6":
        print("Thank you for using the To-Do List Application!")
        break

    else:
        print("Invalid choice. Please try again.")
