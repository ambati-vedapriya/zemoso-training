def decryptCharacters(c):
    k=int(c)-3 
    return chr(k)
def decryptionAlgorithm(str):
    decryptString="" 
    for i in range(0,len(str),3):
        decryptString+=decryptCharacters(str[i:i+3]) 
    return decryptString 
def encryptSingleCharacter(c): 
    k=str(ord(c)+3) 
    if(len(k)<3): 
        return "0"*(3-len(k))+k 
    return k 
def encryptionAlgorithm(str): 
    encryptString="" 
    for i in str: 
        encryptString+=encryptSingleCharacter(i) 
    return encryptString 
n=input("enter code") 
t=encryptionAlgorithm(n) 
print(t) 
print(decryptionAlgorithm(t))

