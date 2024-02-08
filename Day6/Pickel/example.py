# Without pickle

# my_text = "Hello World!"
# my_int = 18
# my_float = 7.657

# with open("mydata.txt",'w') as f:
#     f.write(my_text+'\n')
#     f.write(str(my_int)+'\n')
#     f.write(str(my_float)+'\n')

with open('mydata.txt', 'r') as f:
    data = f.read().splitlines()
    my_text = data[0]
    my_int = int(data[1])
    my_float = float(data[2])

print(my_text)
print(my_int)
print(my_float)

