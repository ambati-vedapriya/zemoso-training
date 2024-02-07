def topTen():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1


values = topTen()
for i in values:
    print(i)


def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)


# generator object with next()

# A generator function
def simpleGeneratorFun1():
    yield 11
    yield 21
    yield 31


# x is a generator object
x = simpleGeneratorFun1()

# Iterating over the generator object using next

# In Python 3, __next__()
print(next(x))
print(next(x))
print(next(x))


# A simple generator for Fibonacci Numbers
def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b

    # Create a generator object


x = fib(5)

# Iterating over the generator object using next
# In Python 3, __next__()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(5):
    print(i)

# generator expression
generator_exp = (i * 5 for i in range(5) if i % 2 == 0)

for i in generator_exp:
    print(i)
