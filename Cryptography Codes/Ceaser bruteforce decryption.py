'''import pycipher
text=str(input("Enter Text:"))
for i in range(0,26):
    print(i,":",pycipher.Caesar(i).decipher(text))'''

def brute(): 
    text=input('enter cipher text: ')
    l1=[]
    
    for ii in range(26):
        result = "" 
        for i in range(len(text)): 
            char = text[i] 
            if (char.isupper()): 
                result += chr((ord(char) - ii-65) % 26 + 65) 
            else: 
                result += chr((ord(char) - ii - 97) % 26 + 97) 
        l1.append(result)
    print(l1)
brute()