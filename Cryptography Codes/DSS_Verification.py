import hashlib as hsh

def modInverse(s, q):
    for i in range(1, q):
        if((s * i) % q == 1):
            return i
    return -1


print('\n Digital Signature Verification')
print('\n Global Public Key Parameters : ')
p = int(input('\n p : '))
q = int(input(' q : '))
g = int(input(' g : '))


y = int(input('\n Public Key - y : '))
hash = int(input('\n Message Hash (int) : ')) 

print(f'\n Signature : ')
r = int(input('\n r : '))
s = int(input(' s : '))

print(f'\n Digital Signature (r, s) : ({r}, {s})')

if ((r >= 1) and (r <= q - 1) and (s >= 1) and (s <= q - 1)):
    w = modInverse(s, q)
    u1 = (hash * w) % q
    u2 = (r * w) % q
    v = (((g ** u1) * (y ** u2)) % p) % q
    print(f'\n w : {w}, u1 : {u1}, u2 : {u2}')
    if v == r:
        print(f'\n v : {v} = r')
        print(f'\n Digital Signature Verification Successful')
    else:
        print(f'\n v : {v} != r')
        print(f'\n Digital Signature Verification Unsuccessful')
else:
    print('\n Invalid Digital Signature') 