n = eval(input("Donnez un nombre : "))

def unite(n):
    return n % 10

def dizaine(n):
    a = n // 10
    return unite(a)

def liste(n):
    
    l = []

    while n > 0:
        l.append(n % 10)
        n = n // 10

    print(l[::-1])
    

liste(n)