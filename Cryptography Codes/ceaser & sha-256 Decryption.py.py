def char_shift(c,n):

	if 97 <= ord(c) <= 127: 
		a = ord(c) - 97
		ch_n = (a + n) % 26 
		return chr(ch_n+97)
	else:					
		a = ord(c) - 65
		ch_n = (a + n) % 26 
		return chr(ch_n+65)

def decrypt(s,n):
	new_str = ""
	n = -n
	for i in s:
		if i.isnumeric():
			new_str += i
		elif i != " ":
			new_str += char_shift(i,n)
	return new_str
  

x=input("Enter cipher text:")
y=int(input("Enter key:"))
text=decrypt(x,y)

print("\nText with hash sha-256:",text)
a,b=text.split("xx")
print("\nMessage is :",a)
print("\nHash value of sha-256:",b)