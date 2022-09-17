# RSA已知n, 密文c, 公钥e, 求明文

import gmpy2
from Crypto.Util.number import long_to_bytes
from Crypto.PublicKey import RSA

public_key = RSA.importKey(open(r"./gy.key", 'rb').read())
n = public_key.n
e = public_key.e

# print(n)
# print(e)

# 通过分解n的质因数得到素数p q
p = 273821108020968288372911424519201044333
q = 280385007186315115828483000867559983517
# 公钥e
e = 65537

n = p * q
z = (p-1) * (q-1)

# 私钥d
d = gmpy2.invert(e, z)
print(d)
# d = 49807846676324857039001173611017456460524559498389088122317223352151924725265

with open('./fllllllag.txt','rb')as f:
    # 密文c
    c = f.read().hex()  # 字符串转16进制
c = int(c, 16)          # 16进制转10进制

# 明文m
m = gmpy2.powmod(c, d, n)
print(long_to_bytes(m))