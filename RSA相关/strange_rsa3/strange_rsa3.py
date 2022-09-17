from Crypto.Util.number import *
from secret import flag3


qBits = 2048
pBits = 512
num = 2
q = getPrime(qBits)
p = [getPrime(pBits) for _ in range(num)]
r = [getRandomRange(1, 2**(pBits * 2))]

a = getRandomRange(1, 2**pBits)
gift = (p[0] * a - p[1]) * inverse(getRandomRange(1, 2**pBits), p[0] * p[1]**2) % (p[0] * p[1]**2)
r.append(a * r[0] % p[1]**2)

n = [p[i] * q + r[i] for i in range(num)]
e = 0x10001
c = pow(bytes_to_long(flag3), e, q)

output = open('output.txt', 'w')
output.write('n = ' + str(n) + '\n')
output.write('c = ' + str(c) + '\n')
output.write('gift = ' + str(gift) + '\n')



