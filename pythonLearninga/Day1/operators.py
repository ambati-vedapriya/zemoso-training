#Arthmetic operator
import math

x,y=2,3
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
#Assingment operators
x+=2
print(x)
x*=2
print(x)
x/=2
print(x)

#Unary operator
n=7
print(-n)
#Relational operator
a,b=5,6
print(a<b)
print(a>b)
print(a==b)
print(a<=b)
print(a>=b)
print(a!=b)

#logical operators
'''
and - 
x y c
0 0 0
0 1 0
1 0 0
1 1 1 //true
or-
x y c
0 0 0
0 1 1 //true
1 0 1 //true
1 1 1 //true



not
'''
a,b=5,4
print("rel")
print(a<8 and b<5)
print(a<4 or b<2)
x=True
print(not (x))

#decimal(base 10) binary(base 2)
#octal(base 8 hexadecimal(base 16)
print(bin(25))
print(0b11001)
print(oct(25))
print(hex(25))
print(hex(10))
print(0xf)

#Bitwise
'''
complement(~) 12- 00001100 11110011
00001100
00001101
---------
00001100 ->&
00001101 ->|

xor-^
x y c
0 0 0
0 1 1 //true
1 0 1 //true
1 1 0 

001010 .000<<2
101000
000010
'''
print(~12)
print(12 & 13)
print(12 | 13)
print(25&21)
print(12^13)
#left shift
print(10<<2)
print(10>>2)

print(math.sqrt(4))
print(math.ceil(2.9))#highest integer
print(math.ceil(2.3))
print(math.floor(2.9))
print(math.floor(2.3))#lowest integer
print(math.pow(2,3))
print(math.pi)
print(math.e)
import math as m
print(m.pi)

a, b = 10, 20

print((b,a)[a < b])