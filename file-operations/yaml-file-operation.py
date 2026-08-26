import yaml
with open("config.yaml", "r") as file:
    data = yaml.safe_load(file)
    print(data["application"]["name"])
    print(data["application"]["version"])
    print(data["database"]["host"])
    print(data["database"]["port"])

    for employee in data["employees"]:
        if employee["name"] == "Khushboo":
            print(employee["department"])

try:
    with open("config.yaml", "r") as file:
        data = yaml.safe_load(file)
        print(data["application"]["name"])

    for employee in data["employees"]:
        print(employee["name"])

    data["database"]["host"] = "production-db"
    data["application"]["debug"] = False

    new_employee = {
            "name": "David",
            "department": "IT"
        }

    data["employees"].append(new_employee)

    with open("config_updated.yaml", "w") as file:
        yaml.safe_dump(data, file)

except FileNotFoundError:
    print("File not found!")

except yaml.YAMLError:
    print("Invalid YAML!")