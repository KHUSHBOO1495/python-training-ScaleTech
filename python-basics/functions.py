def greet(name):
    print(f"Hello, {name}")

greet("Khushboo")

# parameters and arguments
def calculate_total(price, quantity):
    print(price * quantity)
calculate_total(10, 5)

# keyword arguments
calculate_total(price=4, quantity=10)

# default parameters
def greeting(name, message="Hello"):
    print(f"{message}, {name}")
greeting("Khushboo")

# return values
def calculate(a, b):
    return a + b
calculate(5, 10)

# *args/**kwargs

def demo(*args):
    print(args)

demo(10, 20, 30)

# --------------------------

def student(**kwargs):
    print(kwargs)

student(name="Khushboo", age=21, city="Morbi")

# -----------------------------

numbers = [10, 20, 30]

print(*numbers)

# ---------------------------

def employee_info(name, department):
    print(name, department)

employee = {
    "name": "Khushboo",
    "department": "Engineering"
}

employee_info(**employee)

# Scope

# local
def name():
    name = "Khushboo"
    print(name)

name()

# global
n = 10

def num():
    print(n)

num()

# local vs global
a = 15

def number():
    b = 13
    print(b)

number()
print(a)

# global keyword
count = 0

def increase():
    global count
    count += 1

increase()
increase()
print(count)