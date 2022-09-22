# ref: http://mslc.ctf.su/wp/0ctf-2016-quals-rsa-crypto-2-pts/

from re import X
import gmpy2
from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.PublicKey import RSA

n = 23292710978670380403641273270002884747060006568046290011918413375473934024039715180540887338067
e = 3

# 通过分解n的质因数得到素数p q r
p = 26440615366395242196516853423447
q = 27038194053540661979045656526063
r = 32581479300404876772405716877547

with open('./flag.enc','rb')as f:
    c = f.read()
c = bytes_to_long(c)

n = p * q * r
z = (p-1) * (q-1) * (r-1)

# 私钥d
is_perfect = gmpy2.gcd(e, z)
print(is_perfect)
# e和z不互质, 最大公约数为3, 因此不能直接通过e,z逆模求出d --> d = gmpy2.invert(e, z)不可行
# 因此 c = (m^e)^3 mod n --> 需要密文中的模立方根(mod n)
# 因为仅能在有限域求得模根, 所以不能直接对n进行计算 --> n不是素数,不是有限域
# 因此需要计算p,q,r三个素数的三次模根 --> 合并根

# method 1
# pt^3 mod p = c mod p
# pt^3 mod q = c mod q
# pt^3 mod r = c mod r
# 利用在线网站计算pt得 https://www.wolframalpha.com/input?i=x%5E3+%3D+20827907988103030784078915883129+%28mod+26440615366395242196516853423447%29

roots0 = [5686385026105901867473638678946, 7379361747422713811654086477766, 13374868592866626517389128266735]
roots1 = [19616973567618515464515107624812]
roots2 = [6149264605288583791069539134541, 13028011585706956936052628027629, 13404203109409336045283549715377]

# 对这些根应用高斯算法计算
def guass(c0, c1, c2, n0, n1, n2):
    N = n0 * n1 * n2
    N0 = N // n0
    N1 = N // n1
    N2 = N // n2
    d0 = gmpy2.invert(N0, n0)
    d1 = gmpy2.invert(N1, n1)
    d2 = gmpy2.invert(N2, n2)
    return ((c0*N0*d0 + c1*N1*d1 + c2*N2*d2) % N)

for r0 in roots0:
    for r1 in roots1:
        for r2 in roots2:
            M = guass(r0, r1, r2, p, q, r)
            print(long_to_bytes(M))




# method 2

# CipollaLehmer algorithm
# ref: 2013-024.pdf
# sage在线 https://sagecell.sagemath.org/
def cube_root(a,q):
    F = GF(q)
    R.<x> = PolynomialRing(F)
    while 1:
        a = F.random_element()
        b = F.random_element()
        fx = x**3 - a*x**2 + b*x - c
        fc = list(factor(fx))
        if len(fc) <= 1:
            root = pow(x, (q**2+q+1)/3, fx)
            root %= x
            return int(root)
            # return some cube root, but we need to get all of them (at most 3) modulo mach prime

mods = [p, q, r]
rems = []
for mod in mods:
    rems.append([])
    if gcd(mod - 1, 3) == 1:
        d = inverse_mod(3, mod - 1)
        rems[-1].append( int(pow(c, d, mod)) )
    else:
        g = GF(mod).multiplicative_generator()
        u = int(g ** ((mod-1)/3))
        r1 = int(cube_root(c, mod))
        for i in xrange(3):
            rems[-1].append( int(r1 * pow(u, i, mod) % mod) )
    print (rems[-1])
 
from itertools import product
for testrems in product(*rems):
    m = crt(list(testrems), mods)
    assert pow(m, 3, p*q*r) == c % (p*q*r)
    h = hex(m)
    if len(h) & 1:
        h = "0" + h
    print (h.decode("hex"))



