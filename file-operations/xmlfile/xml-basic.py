import xml.etree.ElementTree as ET

tree = ET.parse("employees.xml")
root = tree.getroot()
print(root)
print(root.tag)

for child in root:
    print(child.tag)

employees = root.findall("employee")

for employee in employees:
    print(employee.find("name").text)

for employee in employees:
    print(employee.find("name").text, " - ", employee.find("department").text)

for employee in employees:
    print(employee.get("id"), " - ", employee.find("name").text, " - ", employee.get("active"))

import xml.etree.ElementTree as ET

try:
    tree = ET.parse("employees.xml")
    root = tree.getroot()
    employees = root.findall("employee")

    for employee in employees:
        print(employee.find("name").text)

    for employee in employees:
        if employee.find("department").text == "IT":
            print(employee.find("name").text)

    for employee in employees:
        if employee.find("name").text == "Sarah":
            employee.find("department").text = "Finance"
            
    new_employee = ET.SubElement(root, "employee")
    new_employee.set("id", "104")
    new_employee.set("active", "true")

    name = ET.SubElement(new_employee, "name")
    name.text = "Tejasvi"

    department = ET.SubElement(new_employee, "department")
    department.text = "IT"

    tree.write("employees_updated.xml")

except FileNotFoundError:
    print("File not found!")

except ET.ParseError:
    print("Invalid XML!")

new_employee = ET.SubElement(root, "employee")
new_employee.set("id", "104")
new_employee.set("active", "true")
name = ET.SubElement(new_employee, "name")
name.text = "Tejasvi"

department = ET.SubElement(new_employee, "department")
department.text = "IT"

tree.write("employees_updated.xml")