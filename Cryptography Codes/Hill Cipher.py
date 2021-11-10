import string
key=[]
plaintext=[]

message=input("Enter message : ")
message=message.lower()
message=''.join(message.split())
plaintext[:0]=message


secret=input("Enter Key : ")
secret=secret.lower()
secret=''.join(secret.split())
key[:0]=secret
i=0

while(len(key)!=(i-1)*(i-1)):
    if(len(key)<(i*i)):
        c=len(key)
        for i in range(0,(i*i)-c):
            key.append('x')
    i+=1
print(key)

nXn=i-1
key_m=[]
for i in range(0,len(key),(nXn)):
    temp=[]
    temp=(key[i:(i+nXn)])
    key_m.append(temp)

while(len(plaintext)%nXn!=0): 
    plaintext.append('x')
plaintext_m=[]

for i in range(0,nXn):
    temp=[]
    for j in range(i,len(plaintext),nXn):
        temp.append(plaintext[j])
    plaintext_m.append(temp)

print("\n----------------------\n\t Matrix \n----------------------\n")
print("Key Matrix: ")

for i in key_m:
    print(i)
print("\nPlaintext matrix: ")

for i in plaintext_m:
    print(i)

cipher=[]
for i in range(0,len(plaintext_m[0])):
    for j in range(0,nXn):
        sum=0
        for k in range(0,nXn):
            multi=(ord(key_m[j][k])-97)* (ord(plaintext_m[k][i])-97)
            sum+=multi
        c=sum%26
        cipher.append(string.ascii_lowercase[c])
print("Cipher Text Is : ",cipher)