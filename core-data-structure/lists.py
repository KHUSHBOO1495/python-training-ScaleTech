# list: ordered and mutable
numbers = [1, 2, 3,]
print(numbers[1])
print(numbers[-1])
numbers + [8,9] # does not change the original list

print("before: ",numbers)
numbers.append(4) # can pass only one argument
print("after append: ",numbers)
# numbers.append([5,6])
# numbers.extend((5,6))
numbers.extend([5,6]) # can pass an iterable as an arguments
print("after extend: ",numbers)

# in and not in
6 in numbers # -> True

# insert
numbers.insert(0, 10) # insert at index 0

# delete
numbers.pop() # removes the last element
numbers.pop(1) # removes the element at index 1

numbers.remove(3) # removes the first occurrence of 3

numbers.clear() # removes all elements from the list

# slicing
numbers[1:3] # [2, 3]
numbers[:3] # first 3
numbers[2:] # from index 2 onward
numbers[:] # entire list
numbers[::2] # every second item
numbers[::-1] # reverse

# sort
numbers.sort() # ascending order
numbers.sort(reverse=True) # descending order
numbers.reverse() # reverse the list

# sort vs sorted
numbers.sort() # sorts the original list
new_list = sorted(numbers) # returns a new sorted list

# Heterogeneous list
l1 = [1,'a']
print(l1)

# list comprehension
l1 = [i for i in range(1,6)] # -> [1, 2, 3, 4, 5]
l1 = [i**2 for i in range(1,6)] # -> [1, 4, 9, 16, 25]

# ------------------------------
a = [1, 2, 3]
b = a
b.append(4)
print(a)

# -------------------------------
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)