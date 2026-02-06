from Crypto.Util.number import *
from sage.all import RealField
from secret import flag1


Bits = 512
p = getPrime(Bits)
q = getPrime(Bits)
n = p * q

gift = RealField(prec=Bits*2)(p) / RealField(prec=Bits*2)(q)
e = 0x10001
m = bytes_to_long(flag1)
c = pow(m, e, n)

output = open('output.txt', 'w')
output.write('n = ' + str(n) + '\n')
output.write('c = ' + str(c) + '\n')
output.write('gift = ' + str(gift) + '\n')
