"""
f=open("MyData.txt",'r+')
print(f.read())
print(f.readline())
print(f.readlines())


print(f.read(5))
print(f.seek(0))
print(f.read(5))
f1.close()
#print(f.readline(4),end="")
#print(f.readline())

1=open('abc.txt','w') #if we don't have file it cratees for you
f1.write("i have studied in AITAM")#if we have anything in file it will ovverides it
print()


f1=open('abc.txt','a') #if we have anything in file it will append
f1.write(",CSE Branch")


for data in f:
    print(data)



b=open('veda.jpg',"rb") #read binary
c=open('veda.jpg',"wb")

for i in b:
    c.write()"""

# Opening a file
file1 = open('myfile.txt', 'w')
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
s = "Hello\n"

# Writing a string to file
file1.write(s)

# Writing multiple strings
# at a time
file1.writelines(L)

# Closing file
file1.close()

# Checking if the data is
# written to file or not
file1 = open('myfile.txt', 'r')
print(file1.read())
file1.close()