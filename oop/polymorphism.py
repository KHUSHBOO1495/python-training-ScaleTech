class Animal:
    def sound(self):
        print("Animal makes sound")

class dog(Animal):
    def sound(self):
        super().sound()  # calling parent class method
        print("Dog barks")

class cat(Animal):
    def sound(self):
        print("Cat meows")

animals = [dog(), cat()]
for animal in animals:
    animal.sound()  # polymorphism