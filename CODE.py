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

elif Vopros == 1:
    print("Enter Private Key")
    d = int(input("d = "))
    n = int(input("n = "))
    c = int(input("Enter what need to decrypt  = "))  # i*e % F = 1 !@! i*d = 1 (mod F)
    M = (c ** d) % n
    print("Decrypt message = ",M)
