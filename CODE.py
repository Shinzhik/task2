
from math import gcd
import sympy

Vopros = int(input("For Encryption Enter 0, For Decryption Enter 1 = "))
if Vopros == 0:
    print("Enter prime numbers")
    while True:
        p = int(input("p = "))
        q = int(input("q = "))
        if sympy.isprime(q) == False or sympy.isprime(p) == False:
            print("Enter ONLY PRIME numbers")
        else:
            break

    n = p * q

while True:
        M = int(input('Message: '))
        if M>=n:
            print("Enter a Message less")
        else:
            break



    F = (p - 1) * (q - 1)
    for i in range(2, F):
        if (gcd(i, F) == 1):
            e = i
            break
i = 0
    while (i * e % F != 1):
        i += 1
        d = i
        if i == e:
            i += 1
    C = M ** e % n
    print("crypt message: ",C)
    print(e)
    print(d)
    print(n)

elif Vopros == 1:
    print("Enter Private Key")
    d = int(input("d = "))
    n = int(input("n = "))
    c = int(input("Enter what need to decrypt  = "))  # i*e % F = 1 !@! i*d = 1 (mod F)
    M = (c ** d) % n
    print("Decrypt message = ",M)

