def gcd(a, b):
    # 求解最大公因数 
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def sort_xyz(x, y, z):
    l = [x, y, z]
    l.sort()
    return l

def gcd3(x, y, z):
    # 辗转相除法
    x, y, z = sort_xyz(x, y, z)
    while y != 0:
        temp = y
        y = x % y
        x = temp
    if x < z:
        temp = x
        x = z
        z = temp
    while z != 0:
        temp = z
        z = x % z
        x = temp
    return x

e = 65537

# g = gmpy2.gcd(a, b)

# n1 = 
# c1 = 

# n2 = 
# c2 = 
# P = gcd(n1, n2)
# # print(P)

# Q1 = n1 // P
# Q2 = n2 // P

# Z1 = (P-1) * (Q1-1)
# Z2 = (P-1) * (Q2-1)

# d1 = gmpy2.invert(e, int(Z1))
# d2 = gmpy2.invert(e, int(Z2))

# m1 = gmpy2.powmod(c1, d1, n1)
# m2 = gmpy2.powmod(c2, d2, n2)

# print(long_to_bytes(m1))
# print(long_to_bytes(m2))