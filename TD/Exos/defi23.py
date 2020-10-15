def unites(u):
    return u % 10

def dizaine(d):
    return unites(d // 10)

ValidNumbers = []

def check(p, a, b):
    if unites(p) == b:
        prima = 0
        newP = str(p)[::-1][1:]
        for char in newP:
            if int(char) == 0:
                return
            prima += int(char)

        if prima == a:
            ValidNumbers.append(p)

def parent(n):
    b = unites(n)
    a = dizaine(n)
    for i in range (0, 10**(a+1)):
        check(i, a, b)
    print(ValidNumbers)

parent(31)