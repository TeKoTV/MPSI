def conversion(h,m,s):
    return h * 3600 + m * 3600 + s

def difference(s1, s2):
    return abs(s1 - s2)

print(difference(conversion(8,53,15), conversion(10,27,12)))