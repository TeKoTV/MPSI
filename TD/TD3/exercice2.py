def somme(n):
    a = 0
    for i in range(1, n+1):
        a += i
    return a

def produit(n):
    a = 1
    for i in range(1, n+1):
        a *= i
    return a



print(somme(5)) # Retourne 1+2+3+4+5 = 15
print(produit(5)) # Retourne 1*2*3*4*5 = 120