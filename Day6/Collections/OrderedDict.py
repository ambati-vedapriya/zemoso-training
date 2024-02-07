'''
OrderedDict is a dictionary subclass that remembers the order in which items were inserted.

'''

from collections import OrderedDict

# Create an OrderedDict
ordered_dict = OrderedDict([('one', 1), ('two', 2), ('three', 3)])

# Iterating through items maintains the insertion order
for key, value in ordered_dict.items():
    print(key, value)


Dict = {1: 'veda', 2: 'ambati', 4: 'priya'}
print(Dict)