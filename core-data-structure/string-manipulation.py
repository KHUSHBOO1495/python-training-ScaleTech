name = "Khsuhboo"
department = 'Engineering'
message = """This is
a multi-line
string."""

# indexing
name = "Python"
print(name[0])
print(name[-1])

# slicing
text = "Python Programming"
print(text[0:9])

# Changing Case
text = "python programming"
text.upper()
text.lower()
text.capitalize()
text.title()

name = "   Khushboo   "
print(name.strip()) # remove space from both side

name.lstrip()   # left side
name.rstrip()   # right side

print(text.find("Programming"))
text.find("Java") # -1

text.index("Python")

# find()  → -1 if not found
# index() → ValueError if not found

text.startswith("Py")
text.endswith("ing")
text.isdigit()
text.isalpha()
text.isalnum()
text.isspace()
text.islower()
text.isupper()

# replace
text = "Java Programming"
text = text.replace("Java", "Python")
print(text)

# split
data = "Khushboo,Payal,Tejasvi"
names = data.split(",")

# join
result = ", ".join(names)
print(result)

# removing character from ends
text = "###Python###"
print(text.strip("#"))

# removeprefix() and removesuffix()
url = "https://example.com"
url = url.removeprefix("https://")
print(url)

# Case-insensitive Comparison
is_valid = "YES"
if is_valid.lower() == "yes":
    pass

if is_valid.casefold() == "yes":
    pass