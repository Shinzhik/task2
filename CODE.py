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