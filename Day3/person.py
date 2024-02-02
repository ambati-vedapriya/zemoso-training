class person:
    def __init__(self):
        self.name="veda"
        self.age=21
    def update(self):
        self.age=30

    def compare(self,other):
        if self.age == other.age:
            return  True
        else:
            return False




c1=person()
c2=person()
c2.age=30
c1.update()
if c1.compare(c2):
    print("thery are same age")
else:
    print("they are not same age")
c1.update()

print(a:=1<10) #walrus operator

#instead of pass we  can use  ...
