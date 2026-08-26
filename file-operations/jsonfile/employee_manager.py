import json
try:
    with open("employee.json", "r") as file:
        data = json.load(file)

    print(data["company"])
    for employee in data["employees"]:
        print(employee["name"])

    for employee in data["employees"]:
        if employee["active"]:
            print(employee["name"])

    for employee in data["employees"]:
        if employee["department"]=="IT":
            print(employee)

    new_employee = {"id": 104,
        "name": "David",
        "department": "IT",
        "skills": ["Python", "Docker"],
        "active": True}
    
    data["employees"].append(new_employee)

    with open("employee.json", "w") as file:
        json.dump(data, file, indent=4)


except FileNotFoundError:
    print("File not found!")
except json.JSONDecodeError:
    print("Invalid JSON")