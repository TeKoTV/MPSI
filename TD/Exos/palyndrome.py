# V1
def palyndrome1(p):
    rev = p[::-1]

    return print(str.lower(rev) == str.lower(p))

#V2 (finale)
def palyndrome(p):
    p = str.lower(p)
    wordSize = len(p)
    check = True

    for i in range (0,wordSize):
        if (p[i] != p[wordSize-i-1]):
            check = False
    return print(p, ":", check)

palyndrome("KayAk")
palyndrome("abcd")