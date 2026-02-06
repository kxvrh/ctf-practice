from Crypto.Util.number import *
from secret import flag1, flag2


def generate_poly(modulus, num, root):
    poly = []
    res = 0
    for i in range(1, num+1):
        poly.append(getRandomRange(1, modulus-1))
        res = (res + poly[-1] * pow(root, i, modulus)) % modulus
    return [modulus-res] + poly


Bits = 512
p = getPrime(Bits)
q = getPrime(Bits)
n = p * q

a = getRandomRange(1, p-1)
k = bytes_to_long(flag1)
gift = [generate_poly(p, Bits, a), generate_poly(p, Bits, k * a)]

e = 0x10001
m = bytes_to_long(flag2)
c = pow(m, e, n)

output = open('output.txt', 'w')
output.write('n = ' + str(n) + '\n')
output.write('c = ' + str(c) + '\n')
output.write('gift = ' + str(gift) + '\n')
