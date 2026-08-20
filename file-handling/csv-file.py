import csv

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'department', 'age'])
    writer.writerow(['Khushboo', 'CSE', '21'])
    writer.writerow(['Payal', 'MCA', '22'])
    writer.writerow(['Preksha', 'BCA', '20'])

with open("data.csv", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# skipping the header row
with open("data.csv", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)

# access columns
with open("data.csv", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        name = row[0]
        department = row[1]
        age = int(row[2])

        print(name, department, age)

with open("data.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
