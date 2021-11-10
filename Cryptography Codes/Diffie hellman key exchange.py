from random import randint

Prime = int(input("Enter common prime number:"))
    
primitiveroot = int(input("Enter primitive root:"))
a = int(input('Enter the private key for sender:'))
x = int(pow(primitiveroot,a,Prime))

b = int(input('Enter the private key for receiver:'))    
y = int(pow(primitiveroot,b,Prime))
    
ka = int(pow(y,a,Prime))
kb = int(pow(x,b,Prime))
    
print('Secret key for the sender is : %d'%(ka))
print('Secret Key for the receiver is : %d'%(kb))
