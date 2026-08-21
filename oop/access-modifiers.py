class Parent:

    def __init__(self):
        self.name = "Parent" # public
        self._value = 10 # protected
        self.__secret = 100 # private


obj = Parent()

print(obj.name)
print(obj._value)
# print(obj.__secret)

class Account:

    def public_method(self):
        print("Public")

    def _internal_method(self):
        print("Internal")

    def __private_method(self):
        print("Private")


# new line
print("Hello\nWorld")
# tab
print("Name:\tAlice")
# quote
print("He said \"Hello\"")
print('He said "Hello"')
# backslash
print("C:\\Users\\")