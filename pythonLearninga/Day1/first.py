num=2.5
print(type(num))
num=5
print(type(num))
num=6+9j
print(type(num))
a=5.6
b=int(a)
c=float(a)
d=6
e=complex(a,d)
print(e)
print(a<d)
print(int(True))
print(int(False))
print(type(b))
print(type(c))
print(range(8))
print(list(range(8)))
print(list(range(2,10,2)))
print("hai")
x = "hello world"
s = x[0:3]
print(s)
s = x[:3]
print(s)
#list methods
nums=[25,12,90,56]
print(nums)
print(nums[2])
print(nums[2:])
print(nums[-1])
names=['veda','priya']
mil=[nums,names]
print(mil)
nums.append(18)
print(nums)
nums.insert(2,45)
print(nums)
nums.remove(18)
print(nums)
nums.pop(2)# index
print(nums)
nums.pop() #last element
print(nums)
del nums[0]
nums.extend([24,35,89])
print(nums)
print(min(nums))
print(max(nums))
print(sum(nums))
print(sorted(nums))
#Tuple methods
tup=(21,36,14,25,56,14,36)
print(tup)
print(tup.count(36))
print(tup[3])
#set methods
s={22,45,78,12,34}
print(s)
s.add(88)
print(s)

Dict = {1: 'veda', 2: 'ambati', 4: 'priya'}
print(Dict)
print(Dict[4])
Dict[2] = 'Welcome'
print(Dict)
print(Dict.get(1))
print(Dict.get(3,'not found'))
keys=['kiran','jinan','harsha']
valuse=['python','java','c']
data=dict(zip(keys,valuse))
print(data)
data['mounika']="c++"
print(data)
del data['harsha']
print(data)
print(Dict.items())
print(Dict.keys())
Dict.pop(2)
print(Dict)
Dict.update({3: "Scala"})
print(Dict)
del(Dict[1])
print(Dict)
prog={"js":"atom","cs":"vs","python":["pycharm","subline"],"java":{"JSE":"Netbeans","JEE":"ECLIPSE"}}
print(prog["python"])
print(prog["java"]["JEE"])