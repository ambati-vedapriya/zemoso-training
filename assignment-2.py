def decryptCharacters(encryt_data):
    charcters=int(encryt_data)-3 
    return chr(charcters)
def decryptionAlgorithm(str):
    decryptString="" 
    for i in range(0,len(str),3):
        decryptString+=decryptCharacters(str[i:i+3]) 
    return decryptString 
def encryptSingleCharacter(c): 
    charcters=str(ord(c)+3) 
    if(len(charcters)<3): 
        return "0"*(3-len(charcters))+charcters 
    return charcters 
def encryptionAlgorithm(str): 
    encryptString="" 
    for i in str: 
        encryptString+=encryptSingleCharacter(i) 
    return encryptString 
data=input("enter data u want to send") 
encryt_data=encryptionAlgorithm(data) 
print(encryt_data) 
print(decryptionAlgorithm(encryt_data))

