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
