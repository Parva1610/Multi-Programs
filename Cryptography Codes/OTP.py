import random
charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
def encrypt(plaintext):
    otp = "".join(random.sample(charset, len(charset)))
    result = ""

    for c in plaintext.upper():
        if c not in otp:
            continue
        else:
            result += otp[charset.find(c)]
    return otp, result

def decrypt(otp, secret):
    result = ""
    for c in secret.upper():
        if c not in otp:
            continue
        else:
            result += charset[otp.find(c)]
    return result

Msg = input("Enter Your Message: ")

encrypted = encrypt(Msg)
decrypted = decrypt(encrypted[0], encrypted[1])

print("\nCharset: " + charset)
print("OTP:   \t" + encrypted[0])
print("Encrypted Msg: " + encrypted[1])
print("Decrypted Msg: " + decrypted)
