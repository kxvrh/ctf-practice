# RSA
# 已知多组n, c, 共同e, 利用中国剩余定理

import gmpy2
import libnum
from Crypto.Util.number import long_to_bytes
from Crypto.PublicKey import RSA
from sympy.ntheory.modular import crt

ns = [,,]
cs = [,,]
# cs = [pow(M, e, n) for n in ns]
e = 
g1 = gmpy2.gcd(ns[0], ns[1])
g2 = gmpy2.gcd(ns[0], ns[2])
g3 = gmpy2.gcd(ns[1], ns[2])
# n1, n2, n3最大公约数为1

# sympy库的中国剩余定理 --> crt(ns, cs)直接求出m的e次方
resultant, mod = crt(ns, cs)

# 开方得m
M, is_perfect = gmpy2.iroot(resultant, e)
print(long_to_bytes(M))


