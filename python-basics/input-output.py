name = input("Enter employee name: ")
department = input("Enter department: ")
experience = int(input("Enter experience: "))

print("\nEmployee Details")
print("----------------")
print("Name:", name)
print("Department:", department)
print("Experience:", experience, "years")

# formatting
print('Name: %s, Department: %s, Experience: %d years' % (name, department, experience))

print('Name: {}, Department: {}, Experience: {} years'.format(name, department, experience))

print(f'Name: {name}, Department: {department}, Experience: {experience} years')