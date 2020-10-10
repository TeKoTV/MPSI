z = eval(input("U0 = : "))

def suite(u, n):
    for k in range(0, n+1):
        u = fctn(u)
        k = k # POUR QUE L'IDE ARRÊTE DE ME FAIRE DES PUTAINS D'ERREURS
    print("U", n, " = ", u)

def fctn(u):
    return (2 * u + 1) / (u + 2)
    
suite(2, 10)