# Demander N
n = eval(input("N = "))

print("Table des n :")

def mul(n):
    # Boucle de 1 à 10
    for i in range (1,11):

        # Afficher le résultat
        print(n,"x", i, " = ", n*i)

mul(n)