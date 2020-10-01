t = float(input("Donnez votre taille :"))
m = int(input("Donnez votre poids :"))

imc = m/(t**2)

imc = round(imc * 100) / 100

print("Vous mesurez ", t, " et pesez ", m, "kg et votre IMC vaut", imc)