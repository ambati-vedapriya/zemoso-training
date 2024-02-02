class Computer:
    def __init__(self, cpu, ram):  # it is going to call automatically
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print('config is', self.cpu, self.ram)


com1 = Computer('i5', 16)
com2 = Computer('Ry zen 3', 8)
# Computer.config(com1)
# Computer.config(com2)

com1.config()
com2.config()


class Car:
    wheels = 4  # class variable

    def __init__(self):
        self.mil = 10  # Instance variable
        self.com = "BMW"


c1 = Car()
c2 = Car()
c2.mil = 30
Car.wheels = 8
print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)


class Student:
    school = 'narayana'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):  # instance method -its work with obj
        return (self.m1 + self.m2 + self.m3) / 3

    def get_m1(self):
        return self.m1

    def set_m1(self, value):
        self.m1 = value

    @classmethod
    def getSchool(cls):  # Class method
        return cls.school

    @staticmethod
    def info():
        print("this is student calss")


s1 = Student(34, 56, 78)
s2 = Student(89, 32, 14)
print()
print(s1.avg())
print(s2.avg())
print(Student.getSchool())
Student.info()


class Student_details:
    def __init__(self, name, roll):
        self.name=name
        self.roll=roll
        self.lap=self.Laptop()

    def show(self):
        print(self.name,self.roll)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand='HP'
            self.cpu='i5'
            self.ram=8

        def show(self):
            print(self.ram,self.brand,self.cpu)


s1=Student_details('veda',571)
s2=Student_details('priya',678)
s1.show()
print(s1.lap.brand)
lap1=s1.lap
lap2=Student_details.Laptop()

