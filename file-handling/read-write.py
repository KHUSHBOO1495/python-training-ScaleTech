file = open("demo.txt")
print(file.read())
file.close()

with open("demo.txt") as file:
    data = file.read()
print(data)

with open("demo.txt") as file:
    for line in file:
        print(line)

with open("demo.txt") as file:
    line = file.readline()
    print(line)

with open("demo.txt") as file:
    lines = file.readlines()
print(lines)

with open("demo1.txt", "w") as file:
    file.write("Write operation performed!\n")
    file.write("Hi!\n")

with open("demo1.txt", "a") as file:
    file.write("Append at the end!\n")

with open("new_file.txt", "x") as file:
    file.write("Hello")


# r -> Read
# w -> Write / overwrite
# a -> Append
# x -> Create new file; fail if it exists
# r+ -> Read + write
# b -> Binary mode