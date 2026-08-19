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