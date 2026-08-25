from itertools import combinations, permutations, product, chain, groupby

people = ["Khushboo", "Payal", "Tejasvi"]
result = combinations(people, 2)
print(list(result))

result = permutations(people, 2)
print(list(result))

colors = ["Red", "Blue"]
sizes = ["S", "M", "L"]
result = product(colors, sizes)
print(list(result))

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = chain(numbers1, numbers2)
print(list(result))

numbers = [1, 1, 2, 2, 1, 1]
for key, group in groupby(numbers):
    print(key, list(group))

employees = [
    ("Khushboo", "IT"),
    ("Payal", "IT"),
    ("Preksha", "HR"),
    ("Tejasvi", "HR"),
    ("Diya", "Sales")
]
for department, employees_group in groupby(
    employees,
    key=lambda employee: employee[1]
):
    print(department, list(employees_group))