from functools import reduce


f = lambda a: a * a
res = f(5)
print(res)
f = lambda a, b: a * a + b
res = f(5, 8)
print(res)

nums = [3, 2, 5, 6, 7,3,8,4]
evens = list(filter(lambda n: n % 2 == 0, nums))

double=list(map(lambda n:n*2,evens))

sum= reduce(lambda a,b:a+b,double)
print(evens)
print(double)
print(sum)

b=[56,89]
it=iter(b)
print(it.__next__())
print(next(it))


class TopTen:
    def __init__(self):
        self.num=1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration

values=TopTen()
for i in values:
    print(i)