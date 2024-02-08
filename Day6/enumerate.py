"""
In Python, enumerate() is a built-in function used to iterate over a sequence (such as a list, tuple, or string)
 while keeping track of both the index and the value of each element.
 It returns an enumerate object, which contains tuples of (index, value) pairs.

 enumerate(iterable, start=0)
iterable: The sequence (list, tuple, string, etc.) to iterate over.
start (optional): The index to start the enumeration. By default, it starts from 0.


"""
# Enumerate over a List
fruits = ['apple', 'banana', 'watermelon']

for index, fruits in enumerate(fruits):
    print(index, fruits)

browsers = ['Chrome', 'Firefox', 'Opera', 'Vivaldi']

# create an enumerable and convert to list
x = list(enumerate(browsers))
print(x)

# Enumerate over a String
word = 'python'

for index, word in enumerate(word):
    print(index, word)

# Specify Start Index
colors = ['red', 'green', 'blue']

for index, color in enumerate(colors, start=1):
    print(index, color)

# Using Enumerate with Zip
names = ['Alice', 'Bob', 'Charlie']
ages = [30, 25, 35]

for index, (name, age) in enumerate(zip(names, ages)):
    print(f"Person {index + 1}: {name} is {age} years old")

# Using Enumerate to Create a Dictionary
names = ['Alice', 'Bob', 'Charlie']

# Create a dictionary with names as keys and their index as values
name_index = {name: index for index, name in enumerate(names)}
print(name_index)

"""
It makes no sense to enumerate on a dictionary, because a dictionary is not a sequence.
A dictionary does not have an index, it’s not always in the same order.
"""
