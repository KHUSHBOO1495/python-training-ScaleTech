from collections import Counter, defaultdict, deque, namedtuple

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
counts = Counter(numbers)
print(counts)

text = "banana"
counts = Counter(text)
print(counts.most_common())
print(counts.most_common(2))

students = defaultdict(list)

students["IT"].append("Khushboo")
students["IT"].append("Payal")
students["HR"].append("Tejasvi")

print(students)

items = deque([1, 2, 3])
items.append(4)
items.appendleft(0)
items.pop()
items.popleft()
print(items)

d = deque(maxlen=3)
d.append(1)
d.append(2)
d.append(3)
d.append(4)
print(d)

Student = namedtuple("Student", ["name", "age", "department"])
student = Student("Khushboo", 22, "IT")
print(student.name)
print(student.age)
print(student.department)