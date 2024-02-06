from Day4 import myModule
import platform as pl

a = myModule.person1["age"]
print(a)

myModule.greeting("Jonathan")

x = pl.system()
print(x)
x = dir(pl)
print(x)