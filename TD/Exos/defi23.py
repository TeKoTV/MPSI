def unites(u):
    return u % 10

def dizaine(d):
    return unites(d // 10)

# n : ab et p : parent

ValidNumbers = []

b = 0
a = 0

def init(n):
    b = unites(n)
    a = dizaine(n)

def check(p):
    if (unites(p) == b):
        ValidNumbers.append(p)
    prima = 0
    newP = str(p)[1:]
    for char in newP:
        prima += int(char)

    print (prima)
    

init(31)
check(121)