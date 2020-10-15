import random

n = eval(input("Donnez un nombre limite : "))

def tst(n):
    a = -1
    b = random.randint(0, n)
    x = 0
    while (b != a):
        x += 1
        a = eval(input("Devinez le nombre : "))
        if (a < b):
            print("C'est plus !")
        elif (a > b):
            print("C'est moins !")
    print("Vous avez gagné ! Le nombre était", b, "vous avez réussi en", x, "coups")

tst(n)