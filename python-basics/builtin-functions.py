numbers = [10, 20, 30, 40]

print(len(numbers))
print(type(numbers))
print(sum(numbers))
print(min(numbers))
print(max(numbers))
print(abs(-10))
print(round(10.25569, 2))

# lambda function
square = lambda x: x * x
print(square(5))

# multiple args
add = lambda a, b: a + b
print(add(10, 20))