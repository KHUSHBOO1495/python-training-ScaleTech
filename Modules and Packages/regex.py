import re

# search vs match
if re.search("Python", "Using Python Programming"): # search anywhere in the string 
    print("found")

re.match("Python", "Python Programming") # match only at the beginning

# [abc] -> match any one inside the []
re.search("[aeiou]", "Hello")

# ranges -> [A-Z] [a-z] [0-9]

# \d -> digit
# \w -> word
# \s -> whitespace
# + -> one or more "\d+"
# * -> zero or more "\d*"
# ? -> zero or one "\d?"
# {n} -> n means times "\d{4}"
# {n, m} -> between n and m "\d{2,4}"
# ^ -> start of the string
# $ -> end of the string
# . -> any character
# | -> or

# search
text = "Phone no: 9876543210"
match = re.search(r"\d{10}", text)
if match:
    print("Phone number found")

# find all
text = "I have 10 - 20 books"
numbers = re.findall(r"\d+", text)
print(numbers)

print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))

text = "khushboo._.@gmail.com or khushboo3012@gmail.com"
emails = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)
print(emails)

pattern = re.compile(r"\d+")
print(pattern.findall("10 apples"))
print(pattern.findall("20 oranges"))

# sub
text = "Phone no: 9876543210"
result = re.sub(r"\d+", "XXXXXXXXXX", text)
print(result)

# split
text = "apple,banana;orange|grape"
items = re.split(r"[,;|]", text)
print(items)

# compile
pattern = re.compile(r"python", re.I) # or re.IGNORECASE
print(pattern.search("PYTHON PROGRAMMING"))

# password
pattern = r"^(?=.*[A-Z])(?=.*\d).{8,}$"
password = input("Enter password: ")
if re.fullmatch(pattern, password):
    print("Valid")
else:
    print("Invalid")