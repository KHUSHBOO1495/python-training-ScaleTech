class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author} - {self.price}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.price})"

book = Book("Basics of programming", "abc", 500)
print(book)
print(repr(book))

class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

team = Team(["member1", "member2", "member3"])
print(len(team))

# --------------------------------------------
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("student", 20)
student2 = Student("student", 20)

print(student1 == student2)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

student1 = Student("student", 20)
student2 = Student("student", 20)

print(student1.__eq__(student2))