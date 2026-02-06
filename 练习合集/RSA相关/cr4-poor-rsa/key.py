#coding=utf-8
import base64
import gmpy2
from Crypto.Util.number import long_to_bytes, bytes_to_long
from base64 import b64decode
import rsa

# -----BEGIN PUBLIC KEY-----
# ME0wDQYJKoZIhvcNAQEBBQADPAAwOQIyUqmeJJ7nzzwMv5Y6AJZhdyvJzfbh4/v8
# bkSgel4PiURXqfgcOuEyrFaD01soulwyQkMCAwEAAQ==
# -----END PUBLIC KEY-----

# http://www.hiencode.com/pub_asys.html --> 得到e, n
e = 65537
n = 833810193564967701912362955539789451139872863794534923259743419423089229206473091408403560311191545764221310666338878019

# 分解n得
p = 863653476616376575308866344984576466644942572246900013156919
q = 965445304326998194798282228842484732438457170595999523426901
z = (p-1) * (q-1)

d = int(gmpy2.invert(e, z))


flag = 'Ni45iH4UnXSttNuf0Oy80+G5J7tm8sBJuDNN7qfTIdEKJow4siF2cpSbP/qIWDjSi+w='
with open('./flag.b64','rb')as file:
    f = file.read()
    c = b64decode(f)
    m = pow(bytes_to_long(c), d, n)
    print(long_to_bytes(m))

str = b64decode("Ni45iH4UnXSttNuf0Oy80+G5J7tm8sBJuDNN7qfTIdEKJow4siF2cpSbP/qIWDjSi+w=")
with open('flag.txt', 'wb')as f:
    f.write(str)
f.close()