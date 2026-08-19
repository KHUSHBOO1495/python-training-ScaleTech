def divide(a ,b):
    try:
        print(a / b)
    except ZeroDivisionError as e:
        print(e)

divide(2,0)

# -------------------------------------

numbers = [10, 20, 30]
try:
    print(numbers[5])

except IndexError:
    print("Index doesn't exist.")

# ------------------------------------------------

try:
    number = int(input())
    result = 10 / number
    print(result)
except ValueError:
    print("Enter valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Execution complete!")

# -----------------------------------------------

try:
    number = int(input("Enter a number: "))
    print(number)
except (ValueError, TypeError):
    print("Invalid value.")

# -----------------------------------------

try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid number.")

else:
    print("Successfully converted:", number)

# user-define exception

class NegativeNumberError(Exception):
    pass

try:
    a = int(input())
    if(a > 0):
        print(a)
    else:
        raise NegativeNumberError
except NegativeNumberError:
    print("Number cannot be negative")

# ------------------------------------------------

class NegativeNumberError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

try:
    a=int(input())
    if(a > 0):
        print(a)
    else:
        raise NegativeNumberError("Number can not be negative")
except NegativeNumberError as e:
    print(e)
