class Person:
    pass

p1 = Person()
p1.name = "Khushboo"
p1.age = 21

p2 = Person()
p2.name = "Payal"
p2.age = 22

print(p1.name, p1.age)
print(p2.name, p2.age)

class Person:
    def __init__(self):   # default constructor
        pass

    def __init__(self, name, age):   # parameterized constructor
        self.name = name
        self.age = age

    @staticmethod  #decorator
    def hello():
        print("hello")

    def get_age(self):
        return self.age

p1 = Person("Khushboo", 21)
p1.hello()
print(p1.get_age())
p2 = Person("Payal", 22)

print(p1.__dict__)