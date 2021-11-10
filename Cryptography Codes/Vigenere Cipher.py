def define_key(Plaintext, key):
    key = list(key+Plaintext)
    if len(Plaintext) == len(key):
        print(key)
    else:
        for i in range(len(Plaintext) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
     
def encrypt(Plaintext, key):
    encrypted_text = []
    for i in range(len(Plaintext)):
        x = (ord(Plaintext[i]) + ord(key[i])) % 26
        x += ord('A')
        encrypted_text.append(chr(x))
    return("" . join(encrypted_text))    

def originalText(encrypted_text, key):
    orig_text = []
    for i in range(len(encrypted_text)):
        x = (ord(encrypted_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))
     

Plaintext = input("Enter Plain Text in letters: ").upper()
keyword = input("Enter Keyword: ")
key = define_key(Plaintext, keyword)
encrypted_text = encrypt(Plaintext,key)
print("Cipher text :", encrypted_text)
print("Original/Decrypted Text :", originalText(encrypted_text, key))

