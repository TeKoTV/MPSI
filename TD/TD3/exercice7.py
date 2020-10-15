def occur(w, l):
    a = 0
    for i in range(len(w)):
        if (w[i] == l):
            a += 1
    print("Il y a", a, "fois la lettre \"", l, "\" dans le mot \"", w, "\"")

def occurc(w, l):
    a = []
    for i in range(len(w)):
        if (w[i] == l):
            a.append(i+1)
    print("Il y a", len(a), "fois la lettre \"", l, "\" dans le mot \"", w, "\", places :", a)



w = str(input("Donnez un mot : "))
l = str(input("Donnez une lettre : "))
occurc(w, l)