import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def inverse_multiplication(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    for i in range(temp_phi):
        if((e*i)%temp_phi == 1):
            return i

def prime_func(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generate_keypair(p, q):
    if not (prime_func(p) and prime_func(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    n = p * q
    phi = (p-1) * (q-1)
    e = random.randrange(1, phi)
    print("e:",e)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = inverse_multiplication(e, phi)
    print("d:",d)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)
    
p = int(input("Enter a double digit prime number: "))
q = int(input("Enter another double digit prime number (Not same as above): "))
print( "Generating public/private keypairs now ")
public, private = generate_keypair(p, q)

print( "Public key is ", public ," and Private key is ", private)
message = input("Enter a message to encrypt with your private key: ")
encrypted_msg = encrypt(private, message)
print ("Your encrypted message is: ")

print (''.join(map(lambda x: str(x), encrypted_msg)))
print ("Decrypting message with public key ", public )
print ("Your message is:")
print (decrypt(public, encrypted_msg))
