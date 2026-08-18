import math
print(math.sqrt(25))
print(math.ceil(4.2))
print(math.floor(4.8))
print(math.pow(2, 3)) # OR print(2 ** 3)
print(math.factorial(5))

# constants
print(math.pi)
print(math.e)

r = 5
area = math.pi * r ** 2
print(area)

# trigonometric functions
math.sin(45)
math.cos(80)
math.tan(90)

print(math.gcd(12, 18))

# random module
import random
print(random.random())

number = random.randint(1, 10)
print(number)

number = random.randrange(1, 10)

fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits))

print(random.choices(fruits, k=3)) # may return duplicate values

print(random.sample(fruits, k=2)) # will not return duplicate values

number = [1, 2, 3, 4, 5, 6]
random.shuffle(number)
print(number)


random.seed(42)

print(random.randint(1, 100))
print(random.randint(1, 100))