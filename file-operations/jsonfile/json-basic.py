import json

with open("employee.json", "r") as file:
    data =json.load(file)

print(data)


json_data = '{"name": "John", "age": 25}'
data = json.loads(json_data)
print(data)
print(type(data))


employee = {
    "id": 101,
    "name": "Khushboo",
    "department": "CSE",
    "salary": 50000,
    "is_active": True
}
with open("employee_demo.json", "w") as file:
    json.dump(employee, file, indent=4)

employee = {
    "id": 101,
    "name": "Khushboo",
    "department": "CSE"
}
json_string = json.dumps(employee)
print(json_string)


json_response = '''
{
    "id": 101,
    "name": "Khushnoo",
    "department": "IT"
}
'''

# Step 1: JSON string → Python dictionary
employee = json.loads(json_response)

# Step 2: Modify the Python dictionary
employee["department"] = "HR"

# Step 3: Python dictionary → JSON file
with open("updated_employee.json", "w") as file:
    json.dump(employee, file, indent=4)


json_string = '''{
    "id": 101,
    "name": "Khushboo",
    "skills": [
        "Python",
        "SQL",
        "Git"
    ],
    "address": {
        "city": "Ahmedabad",
        "country": "India"
    }
}'''

data = json.loads(json_string)

print(data["name"])
print(data["skills"][1])
print(data["address"]["city"])
print(data["address"]["country"])

with open("employee.json", "r") as file:
    data =json.load(file)

    for employee in data["employees"]:
        if employee["department"]=="IT":
            print(employee)


try:
    with open("employee.json", "r") as file:
        data = json.load(file)
        print(data)

except FileNotFoundError:
    print("File not found.")

except json.JSONDecodeError:
    print("Invalid JSON.")