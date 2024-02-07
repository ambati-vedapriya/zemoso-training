import time


def div(a, b):
    print(a / b)


div(2, 4)


def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner


div1 = smart_div(div)
div1(2, 4)


def f1(func):
    def wrapper():
        print("Started")
        func()
        print("Ended")

    return wrapper


@f1
def f():
    print("hello")


"""f1(f)()

a=f1(f)
a()"""

f()


def f2(func):
    def wrapper(*args, **kwargs):
        print("Started")
        val = func(*args, *kwargs)
        print("Ended")
        return val

    return wrapper


@f2
def b(a, b=9):
    print(a, b)


@f2
def add(x, y):
    return x + y


print(add(4, 5))

"""
def timer(func):
    def wrapper():
        before = time.time()
        func()
        print("function took", time.time() - before, "seconda")

    return wrapper()


@timer
def run():
    time.sleep(2)


run()"""


# decorator to calculate duration
# taken by any function.
def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before Execution")

        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")

        # returning the value to the original frame
        return returned_value

    return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b


a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))


def decor1(func):
    def inner():
        x = func()
        return x * x

    return inner


def decor(func):
    def inner():
        x = func()
        return 2 * x

    return inner


@decor1
@decor
def num():
    return 10


@decor
@decor1
def num2():
    return 10


print(num())
print(num2())

"""decor1(decor(num))
decor(decor1(num2))"""


def decor1(func):
    def wrap1():
        print("************")
        func()
        print("************")

    return wrap1


def decor2(func):
    def wrap():
        print("@@@@@@@@@@@@")
        print("this is one")
        func()
        print("@@@@@@@@@@@@")

    return wrap

@decor1
@decor2
def sayhellogfg():
    print("Hello")


def saygfg():
    print("veda priya")


sayhellogfg()
saygfg()
