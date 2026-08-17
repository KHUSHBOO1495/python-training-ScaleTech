age = 21
is_valid = False

# arithmetic
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# comparison
print(a == b)
print(a != b)
print(a > b)
print(a < b)

# assignment
a = 10
a += 5
a -= 2
a *= 3
a /= 2

# logical
print(a > 5 and b < 5)
print(age >= 18 and is_valid)
print(age >= 18 or is_valid)
print(not is_valid)

# membership
numbers = [1, 2, 3]

print(2 in numbers)
print(5 not in numbers)

# identity
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a == c)

print(a is b)
print(a is c)