# RSA已知n, 密文c, 公钥e, 求明文

import gmpy2
from Crypto.Util.number import *
from Crypto.PublicKey import RSA

n = 87924348264132406875276140514499937145050893665602592992418171647042491658461

# 通过分解n的质因数得到素数p q
p = 275127860351348928173285174381581152299
q = 319576316814478949870590164193048041239
# 公钥e
e = 65537

n = p * q
z = (p-1) * (q-1)

# 私钥d
d = gmpy2.invert(e, z)
print(d)

with open('./flag.enc','rb+')as f:
    # 密文c
    content = f.read()
    c = bytes_to_long(content)

# 明文m
m = gmpy2.powmod(c, d, n)
print(long_to_bytes(m))