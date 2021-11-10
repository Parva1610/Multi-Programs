import hashlib as hsh
import random as r
import math
def prime(ls=[]):
    for i in range(11, 10001):
        for j in range(2, 1 + (i // 2)):
            if i % j == 0:
                break
        else:
            ls.append(i)
    return ls

def public_key_comp():
    ls = prime()
    p = 0
    while p < 2000:
        p = r.choice(ls)
    q = []
    for i in range(2, p):
        if math.gcd(p - 1, i) != 1:
            if i in ls:
                q.append(i)
    q = r.choice(q)
    g = []
    for h in range(1, p - 1):
        x = (h ** ((p - 1) // q)) % p
        if x > 1:
            x = ((h * (p - 1)) // q) % p
            g.append(x)
    g = r.choice(g)
    return p, q, g
    
def modInverse(k, q):
    for i in range(1, q):
        if((k * i) % q == 1):
            return i
    return 0
# global public key parameters
p, q, g = public_key_comp()
# p, q, g = 283, 47, 60

# private key
x = r.randint(1, q-1)
# x = 24

inv_k = 0

while inv_k == 0:

    # per-message secret number
    k = r.randint(1, q - 1)

    # k = 15

    # public key
    y = (g ** x) % p

    # modular inverse of 'k'
    inv_k = modInverse(k, q)

print('\n Digital Signature Algorithm')
print(f'\n Global Public Key Parameters : ', end='')
print(f' p : {p}, q : {q}, g : {g}')

print(f'\n Public Key - y : {y}')
print(f'\n Private Key - x : {x}')
print(f'\n Per-message Secret No. - k : {k}')

msg = input('\n Message : ')

# hash (sha1) converted to integer
hash = int(hsh.sha1(msg.encode()).hexdigest(), 16)
# hash = 41

# signature components
r = ((g ** k) % p) % q
s = (((x * r) + hash) * inv_k) % q

print(f'\n Message Hash (int) : {hash}')
print(f'\n Digital Signature (r, s) : ({r}, {s})') 