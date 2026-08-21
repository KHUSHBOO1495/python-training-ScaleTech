class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"{self.name} earns {self.salary}")

class Developer(Employee):
    def write_code(self):
        print(f"{self.name} is writing code.")

class Tester(Employee):
    def show_details(self):  # method overriding
        print(f"{self.name} is a tester and earns {self.salary}")

    def test_code(self):
        print(f"{self.name} is testing code.")

d1 = Developer("Khushboo", 50000)
d1.show_details()
d1.write_code()

t1 = Tester("Payal", 40000)
t1.show_details()



# Multiple inheritance
class Camera:
    def take_photo(self):
        print("Taking photo")


class Phone:
    def take_photo(self):
        print("Taking photo with phone")
    def make_call(self):
        print("Making call")


class Smartphone(Camera, Phone):
    def play_music(self):
        print("Playing music")

s1 = Smartphone()
s1.take_photo()
s1.make_call()

print(Smartphone.__mro__)  # method resolution order