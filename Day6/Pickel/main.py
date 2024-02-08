import pickle

'''
Pickle in Python is used for serializing and deserializing objects, 
allowing you to save Python objects to a file or transmit them between processes. 

It's useful for:

- Persistence: Saving complex data structures, like dictionaries or custom objects, 
               to a file for later use.

- Data Storage: Efficiently storing large datasets in a binary format.

- Interprocess Communication: Exchanging Python objects between different Python 
                              processes or systems.

- Model Serialization: Saving machine learning models for later use or sharing.

- State Preservation: Preserving the state of an object for later retrieval.

'''


class Person:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def print_info(self):
        print(self.name)
        print(self.age)
        print(self.weight)

    def get_older(self, years):
        self.age += years


p1 = Person("veda", 22, 50)
p1.print_info()
p1.get_older(6)
p1.print_info()

# Dump object into the file => serialization

with open('veda.pickle', 'wb') as f:
    pickle.dump(p1, f)

# Load the object from the file => deserialization

with open('veda.pickle', 'rb') as f:
    p2 = pickle.load(f)

p2.print_info()
