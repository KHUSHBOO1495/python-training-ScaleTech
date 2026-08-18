# Set: unordered, mutable and unique elements
s1 = set() # create empty set

numbers = {10, 20, 30, 20, 10}
print(numbers)

numbers.add(50)
numbers.update([60, 70])
print(numbers)

numbers.update((80, 90))
print(numbers)

numbers.remove(20)

# numbers.remove(40) # error
numbers.discard(40) # no error

numbers.pop()

n = {1, 2, 3, 4, 5, 6, 7}
n1 = {1, 2, 3, 4, 5}
n2 = {4, 5, 6, 7}

# union (n1 + n2)
n1.union(n2) # {1, 2, 3, 4, 5, 6, 7}

# intersection (common elements)
n1.intersection(n2) # {4, 5}

# difference (n1 - n2)
n1.difference(n2) # {1, 2, 3}
n2.difference(n1) # {6, 7}

# symmetric difference
n1.symmetric_difference(n2) # {1, 2, 3, 6, 7}

# subset & superset
n1.issubset(n)
n.issuperset(n2)

# set comprehension
numbers = [1, 2, 3, 4, 5]
squares = {x * x for x in numbers}
print(squares)

# frozenset
s1 = frozenset({1, 2, 3})
# s1.add(4) # X - doesn't work