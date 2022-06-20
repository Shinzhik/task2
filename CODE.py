#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

    n = p * 

