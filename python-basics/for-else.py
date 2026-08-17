numbers = [10, 20, 30, 40, 50]
target = 30
# target = 99

for num in numbers:
    if num == target:
        print("Found!")
        break
else:
    print("Not found!")