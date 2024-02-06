a = 5
b = 4
try:
    print("resourse open")
    print(a / b)
    k = int(input("enter the number"))
    print(k)

except ZeroDivisionError as e:
    print("don't divide by zero", e)
except ValueError as e:
    print("invalid input", e)
except Exception as e:
    print("something went wrong")

finally:
    print("resourse close")

print("done")

try:
    a = [1, 2, 3]
    print(a[3])
except LookupError:
    print("Index out of bound error.")
else:
    print("Success")

#Else

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")



#Raise error
"""x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")

#User-defined errror"""
class MyError(Exception):

    # Constructor or Initializer
    def __init__(self, value):
        self.value = value

    # __str__ is to print() the value
    def __str__(self):
        return (repr(self.value))


try:
    raise (MyError(3 * 2))

# Value of Exception is stored in error
except MyError as error:
    print('A New Exception occurred: ', error.value)