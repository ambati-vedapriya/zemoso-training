class A:  # super class
    def feature(self):
        print("Feature1 is working")

    def feature2(self):
        print("Feature2 is working")


class B(A):  # Class B inheriting the class A(sub class) one -level inheritance
    def feature3(self):
        print("Feature3 is working")

    def feature4(self):
        print("Feature4 is working")


class C(B):  # multilevel inheritance
    def feature5(self):
        print("Feature5 is working")


a1 = A()
b1 = B()
b1.feature()
b1.feature2()
b1.feature3()
c1 = C()
c1.feature5()
c1.feature3()
c1.feature()


class One:  # super class
    def feature(self):
        print("Feature1 is ")

    def feature2(self):
        print("Feature2 is ")


class Two():
    def feature3(self):
        print("Feature3 is ")

    def feature4(self):
        print("Feature4 is ")


class Three(One, Two):  # multiple inheritance
    def feature5(self):
        print("Feature5 is ")


a1 = One()
b1 = Two()
c1 = Three()
c1.feature5()
c1.feature3()
c1.feature()


class First:  # super class

    def __init__(self):
        print("init first")

    def feature(self):
        print("Feature1 is working")

    def feature2(self):
        print("Feature2 is working")


class Second(First):
    def __init__(self):
        super().__init__()
        print("init in second")

    def feature3(self):
        print("Feature3 is working")

    def feature4(self):
        print("Feature4 is working")

'''
if you create obj of subclass it will first try to find out the init of subclass
if it is not found the it will call init of super class
'''
s1 = Second()


class Hello:  # super class

    def __init__(self):
        print("init first hello")

    def feature(self):
        print("Feature1 is hello")

    def feature2(self):
        print("Feature2 is hello")


class Hai():
    def __init__(self):
        print("init in second Hai")

    def feature(self):
        print("Feature1 is Hai")

    def feature4(self):
        print("Feature4 is Hai")

class What(Hai,Hello):
    def __init__(self):
        super().__init__()
        print("init in what")
    def feat(self):
        super().feature2()


'''
MRO- Method resolution order -when we have multiple inheritance left to right
'''
w1 = What()
w1.feature()