"""x=int(input("enter the number"))
if x%2==0 :
    print("even number")
    if x>7 :
        print("great 7")
else:
    print("odd number")


x=int(input("enter the number btw 1to 3"))
if x==1:
    print("one")
elif x==2:
    print("two")
elif x==3:
    print("three")
else:
    print("not in range")"""

#While loop
z=1
while z<=5:
    print("hi",end=" ")
    j=1
    while j<=4:
        print("cinderilla ",end="")
        j=j+1
    z=z+1
    print()

# For loop

y="veda"
for i in y:
    print(i)

for i in ['veda',65,79]:
    print(i)

for i in range(10,2,-1):
    print(i)

for i in range(1,21):
    if i%5!=0:
        print(i)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#he else block will NOT be executed if the loop is stopped by a break statement.
for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")

#break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#Continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

for i in range(1,50):
    if i%2!=0 :
        pass
    else:
        print(i)