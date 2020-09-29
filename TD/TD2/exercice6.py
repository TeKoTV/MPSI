def conversion(h,m,s):
    h *= 3600
    m *= 60
    return h + m + s

def difference(s1, s2):
    return abs(s1 - s2)

print(difference(conversion(8,53,15), conversion(10,27,12)))