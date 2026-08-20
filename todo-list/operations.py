import csv

def load_tasks():
    with open("tasks.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)

def save_tasks(tasks):
    with open("tasks.csv", "w", newline="") as file:
        fieldnames = ["title", "completed"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tasks)

def validate_task_number(task_number, tasks_count):
    if task_number < 0 or task_number >= tasks_count:
        print("Invalid task number.")
        return False

    return True