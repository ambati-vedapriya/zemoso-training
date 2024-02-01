'''
polymorphism can be  implemented in four types
Duck typing
Method Overloading
Method OverRiding
Operator Overloading

many forms
we use it in
loose coupling
interface
Dependency injection
'''

x = 5
x = "veda"


class PyCharm:
    def execute(self):
        print("compiling")


class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")


class Laptop:
    def code(self, ide):
        ide.execute()


ide = MyEditor()
lap1 = Laptop()
lap1.code(ide)


# Method overloading- class contains same name with diff parameters
# Method overriding-we have different class but contain same methods
class Average:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a

        return s


A1 = Average(56, 70)
print("sum is", A1.sum(34, 20))


class A:
    def show(self):
        print("in A show")


class B(A):
    def show(self):  # this show method overrides the A class show
        print("in B show")


a1 = B()
a1.show()

# Operator overloading
a = "hai"
b = "evey"
print(str.__add__(a, b))

a = 4
b = 6
print(int.__add__(a, b))


class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False


s1 = Student(90, 56)
s2 = Student(95, 67)
s3 = s1 + s2
print(s3.m1)

if s1 > s2:
    print('s1 wins')
else:
    print('s2 wins')
