import hashlib

def shift_char(c,n):
	if 97 <= ord(c) <= 127: 
		a = ord(c) - 97
		ch_n = (a + n) % 26 
		return chr(ch_n+97)
	else:				
		a = ord(c) - 65
		ch_n = (a + n) % 26 
		return chr(ch_n+65)

def caesar_encrypt(s,n):
	new_str = ""
	for i in s:
		if i.isnumeric():
			new_str += i
		elif i != " ":
			new_str += shift_char(i,n)
	return new_str


def encrypt_string(hash_string):
	sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
	return sha_signature

message = input("Enter the message :: ")

hash_value = encrypt_string(message)

plain_text = message +'xx'+ hash_value

print("The whole plain text message is ::",plain_text)
Key = int(input("Enter key value:- "))
print("The whole cypher text is \t::",caesar_encrypt(plain_text ,Key))

