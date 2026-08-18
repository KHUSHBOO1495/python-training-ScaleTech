# Dictionary: ordered and mutable
d = {} # empty dictionary

person = {
    "name": "Khushboo",
    "age": 21
}

print(person["name"])

# print(person["city"]) # Error
print(person.get("city")) # returns None if key not found

person["city"] = "Morbi"

person.pop("city")
del person["age"]

person.clear() # removes everything

person = {
    "name": "Khushboo",
    "age": 21,
    "city": "Morbi"
}

print(person.keys())
print(person.values())
print(person.items()) # key value pair

# Tuples can be keys:
locations = {
    (56.2,23.5): "Ahmedabad"
}

# But lists can't:
# data = {
#     [1, 2]: "Khushboo" # Error! Because lists are mutable.
# }

# dictionary comprehension
# {key: value for item in iterable}
numbers = [1, 2, 3, 4, 5]
squares = { x: x * x for x in numbers}
print(squares)

# update dictionary
person = {
    "name": "Khushboo",
    "age": 21
}

person.update({
    "age": 26,
    "city": "Morbi"
})

print(person)

# setdefault
person = {
    "name": "Khushboo"
}

person.setdefault("department", "Engineering")

print(person)

person.setdefault("name", "Payal") # does not change the value of name key
print(person)

# duplicate keys
a = {
    "name": "Khushboo",
    "age": 21
}

b = {
    "age": 52,
    "city": "Rajkot"
}

combined = a | b