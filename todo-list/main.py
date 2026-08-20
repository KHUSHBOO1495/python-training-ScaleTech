from operations import load_tasks, save_tasks, validate_task_number

while True:
    print("\n=== TODO LIST ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose an option:")
    if choice == '5':
        print("Goodbye!")
        break
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please try again.")
        continue

    if choice == '1':

        tasks = load_tasks()

        new_task = {
            "title": input("Enter task title: "),
            "completed": "False"
        }
        tasks.append(new_task)

        save_tasks(tasks)
        print("Task saved!")

    elif choice == '2':
        tasks = load_tasks()
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] == "True" else "Not Completed"
            print(f"{i}. {task['title']} - {status}")

    elif choice == '3':
        tasks = load_tasks()

        try:
            task_number = int(input("Enter task number to complete: ")) - 1
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if not validate_task_number(task_number, len(tasks)):
            continue

        tasks[task_number]["completed"] = "True"

        save_tasks(tasks)
        print("Task completed!")

    elif choice == '4':
        tasks = load_tasks()

        try:
            task_number = int(input("Enter task number to delete: ")) - 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if not validate_task_number(task_number, len(tasks)):
            continue

        tasks.pop(task_number)

        save_tasks(tasks)
        print("Task deleted!")