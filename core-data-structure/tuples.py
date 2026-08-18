# Tuple: heterogeneous, ordered and immutable
num = () # empty tuple

#-------------
x = (10)
print(type(x)) # <>class 'int'>
x = (10,) # OR x = 10,
print(type(x)) # <class 'tuple'>

# tuple packing
t1 = 1,2,2,4,5 # -> <class 'tuple'>

#tuple unpacking
a,b,c,d,e = t1 # a=1, b=2, c=3, d=4, e=5
a,*b = t1 # a=1, b=[2,3,4,5]

t1.count(2) # 2
t1.index(4) # 3

# tuple comprehension
t2 = tuple(i for i in range(1,6)) # -> (1, 2, 3, 4, 5)
t2 = (*(i for i in range(1,6)),) # -> (1, 2, 3, 4, 5)

# conversion
numbers = [10, 20, 30]

# list -> tuple
numbers_tuple = tuple(numbers)
# tuple -> list
numbers_list = list(numbers_tuple)

