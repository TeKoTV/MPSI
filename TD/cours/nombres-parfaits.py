""""

Un nombre parfait est un nombre qui est égal à la somme de ses diviseurs (sauf lui même)

""""



# On créé la fonction nombre parfait (Ici on l'appelle "parf")
def parf(n):

    # s sera la somme des diviseurs
    s = 0

    # On boucle de 1 à (n/2) + 1 (pour retrouver l'ensemble de ses diviseurs)
    for i in range (1, (n // 2) + 1):
        
        # On teste si n est congru à 0 modulo i
        if (n % i == 0):

            # Si c'est le cas, alors on ajoute i à la somme
            s += i

    # Si la somme des diviseurs de n est égale à n, on affiche que n est un nombre parfait (ou pas, si il ne l'est pas)        
    if (s == n):
        print(n, " est un nombre parfait")
    else:
        print(n, " n'est pas un nombre parfait")

# On exécute la fonction pour tester

parf(6)
parf(8)