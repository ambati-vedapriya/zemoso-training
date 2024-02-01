def greet():  # function definition
    print("Hello")
    print("Everyone")


greet()  # function calling


def add_sub(x, y):
    c = x + y
    d = x - y
    return c, d


result1, result2 = add_sub(5, 5)
print(result1, result2)


def update(lst):
    x = 8
    print(id(lst))
    print("lst", lst)


lst = [10, 20, 30]
print(id(lst))
update(lst)
'''
there is no pass by value and pass by reference
different types of arguments
Actual arguments are four types
position
keyword
Default
Variable length

'''


# position argument -we can't exchange position
def person(name, age):
    print("ny name is", name)
    print(age)


person('veda',6)


# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)


# Keyword arguments
student(firstname='veda', lastname='priya')
student(lastname='priya', firstname='veda')


def person(name, year=2001):  # default arguments

    print("ny name is", name)
    print(year)


person(name='veda')


def sum(a, *b):  # Variable length
    c = a
    print(a)
    print(b)
    for i in b:
        c = c + i
    print(c)


sum(5, 6, 1, 2)


def person_data(name, **data):  # keyword variable argument
    print(name)
    print(data)
    for i, j in data.items():
        print(i, j)


person_data('veda', age=28, city='Agra', mob=87978)
