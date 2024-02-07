'''
Counter is a dictionary subclass for counting hashable objects.
It allows you to count the occurrences of elements in a collection.

'''

from collections import Counter

# Create a Counter from a list
counts = Counter(['a', 'b', 'a', 'c', 'b', 'a'])

# Access counts of individual elements
print(counts['a'])
