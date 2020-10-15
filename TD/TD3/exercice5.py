def s(n,m):
    a = 0
    for i in range(0, n+1):
        a += i**m
    print(a)

s(10, 2)