tasks = []

while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Enter your choice: ").strip()
    
    if choice == '1':
        task_description = input("Enter task description: ").strip()
        tasks.append({"description": task_description, "completed": False})
        print(f"Task '{task_description}' added.")
    
    elif choice == '2':
        if not tasks:
            print("No tasks to show.")
        else:
            for index, task in enumerate(tasks):
                status = "Done" if task["completed"] else "Pending"
                print(f"{index + 1}. {task['description']} - {status}")
    
    elif choice == '3':
        try:
            task_number = int(input("Enter task number to mark as completed: ").strip())
            if 0 < task_number <= len(tasks):
                tasks[task_number - 1]["completed"] = True
                print(f"Task {task_number} marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    elif choice == '4':
        try:
            task_number = int(input("Enter task number to delete: ").strip())
            if 0 < task_number <= len(tasks):
                task = tasks.pop(task_number - 1)
                print(f"Task '{task['description']}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    elif choice == '5':
        print("Exiting...")
        break
    
    else:
        print("Invalid choice. Please try again.")
