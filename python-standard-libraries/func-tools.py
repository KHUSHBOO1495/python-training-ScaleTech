def greet(name, message):
    return f"{message}, {name}"
greet("Khushboo", "Hello")
greet("Payal", "Hello")

from functools import partial, reduce, lru_cache
from operator import mul

hello = partial(greet, message="Hello")
print(hello("Khushboo"))
print(hello("Payal"))


def calculate_price(price, tax):
    return price + (price * tax)

calculate_with_tax = partial(calculate_price, tax=0.10)
print(calculate_with_tax(100))
print(calculate_with_tax(500))

numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)
print(result)

def add(x, y):
    return x + y
numbers = [1, 2, 3, 4]
result = reduce(add, numbers)
print(result)

print(reduce(mul, [2, 3, 4]))

@lru_cache
def square(n):
    print("Calculating...")
    return n * n