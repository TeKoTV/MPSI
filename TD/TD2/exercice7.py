def unites(n):
    return n % 10

def dizaine(n):
    a = n // 10
    return unites(a)

def centaine(n):
    a = n // 10
    return dizaine(a)

def Armstrong(m):

    u = unites(m)
    d = dizaine(m)
    c = centaine(m)

    somme = u ** 3 + d ** 3 + c ** 3

    return m == somme

print(Armstrong(153))
print(Armstrong(157))