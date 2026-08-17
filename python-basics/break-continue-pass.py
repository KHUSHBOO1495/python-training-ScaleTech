numbers = range(1, 5)
print(numbers)

for number in range(1, 100):
    if number == 10:
        break
    print(number)

for number in range(1, 11):
    if number % 2 == 0:
        continue
    print(number)

def expected_feature():
    pass