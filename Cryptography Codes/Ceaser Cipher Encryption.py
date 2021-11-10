text=input("Enter Text to be encrypted: ")
key=int(input("Enter key(1 to 25):"))
ans=""
if(key<=25 and key>=1):
   for i in range(len(text)):
      char = text[i]
      if(char.isupper()):
         ans += chr((ord(char) + key - 65)%26 +65)
      else:
         ans += chr((ord(char) + key - 97)%26 +97)
 
else:
   print("Please enter key between 1 and 25")
print(ans)
