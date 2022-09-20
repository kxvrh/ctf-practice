#!/usr/bin/python
# coding=utf-8

import gmpy2  
from Crypto.Util.number import long_to_bytes
c = 9217979941366220275377875095861710925207028551771520610387238734819759256223080175603032167658086669886661302962985046348865181740591251321966682848536331583243529  
m = gmpy2.isqrt(c)  
m = int(m)  
print(long_to_bytes(m))

# Rabin算法 (e=2)
# c = m^2 mod n
# mp = 根号c mod p, mq = 根号c mod q
# 扩展欧几里得计算出yp和yq
# yp * p + yq * q = 1
# 解出四个明文a,b,c,d
# a = (yp*p*mq + yq*q*mp) mod n
# b = n - a
# c = (yp*p*mq - yq*q*mp) mod n
# d = n - c
# 若p ≡ q ≡ 3(mod 4), 则        --> 一般情况是满足的
# mp = c^(1/4 * (p+1)) mod p
# mq = c^(1/4 * (q+1)) mod q
# 若不满足p ≡ q ≡ 3(mod 4), 需要参考相应的算法解决

import gmpy2
import string
from Crypto.PublicKey import RSA

# 读取公钥参数
with open('pubkey.pem', 'r') as f:
    key = RSA.importKey(f)
    N = key.n
    e = key.e
with open('flag.enc', 'r') as f:
    cipher = f.read().encode('hex')
    cipher = string.atoi(cipher, base=16)
    # print(cipher)

# 分解n得到p, q
print ("please input p")
p = int(input(), 10)
print ('please input q')
q = int(input(), 10)
# 计算yp和yq
inv_p = gmpy2.invert(p, q)
inv_q = gmpy2.invert(q, p)

# 计算mp和mq
mp = pow(cipher, (p + 1) / 4, p)
mq = pow(cipher, (q + 1) / 4, q)

# 计算a,b,c,d
a = (inv_p * p * mq + inv_q * q * mp) % N
b = N - int(a)
c = (inv_p * p * mq - inv_q * q * mp) % N
d = N - int(c)

for i in (a, b, c, d):
    print(long_to_bytes(a))
    print(long_to_bytes(b))
    print(long_to_bytes(c))
    print(long_to_bytes(d))
    # s = '%x' % i
    # if len(s) % 2 != 0:
    #     s = '0' + s
    # print(s.decode('hex'))