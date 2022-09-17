# RSA
# 已知p,q,e,c，求m

import gmpy2
from Crypto.Util.number import long_to_bytes

# 素数p q
p = 
q = 

# 公钥e
e = 
# 密文c
c = 
# c = gmpy2.powmod(m, e, n)

n = p * q
z = (p-1) * (q-1)

# 私钥d
d = gmpy2.invert(e, z)

# 明文m
m = gmpy2.powmod(c, d, n)
print(long_to_bytes(m))
