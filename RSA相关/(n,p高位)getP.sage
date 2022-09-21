# 已知n以及p的高位
# 根据Coppersmith partial information attack计算出p (Factoring with high bits known)
# 常规RSA解密

p = 0xd7e990dec6585656512c841ac932edaf048184bac5ebf9967000000000000000
n = 0xb50193dc86a450971312d72cc8794a1d3f4977bcd1584a20c31350ac70365644074c0fb50b090f38d39beb366babd784d6555d6de3be54dad3e87a93a703abdd

# 需要运行sage计算完整的p https://sagecell.sagemath.org/

# 未知的p的低位位数
kbits = 60
PR.<x> = PolynomialRing(Zmod(n))
f = x + p
# x0为求得的p低位
x0 = f.small_roots(X=2^kbits, beta=0.4)[0]
print("x: %s" %hex(int(x0)))
p = p+x0
print ("p: ", hex(int(p)))
assert n % p == 0
q = n//int(p)
print ("q: ", hex(int(q)))


# import gmpy2
# from Crypto.Util.number import long_to_bytes

# n = 0xb50193dc86a450971312d72cc8794a1d3f4977bcd1584a20c31350ac70365644074c0fb50b090f38d39beb366babd784d6555d6de3be54dad3e87a93a703abdd
# e = 0x3
# c = 0x428a95e5712e8aa22f6d4c39ee5ec85f422608c2f141abf22799c1860a5e343068ab55dfb5c99a7085714f4ce8950e85d8ed0a11fce3516cf66a641dca8321ee
# p = 0xd7e990dec6585656512c841ac932edaf048184bac5ebf996707c373ce49e0d8d
# q = 0xd69ce6875fc08851bd9b39ad9d58a1f1ba4cf992a0df2b35034b698629f8bb91

# z = (p-1) * (q-1)
# d = gmpy2.invert(e, z)
# m = gmpy2.powmod(c, d, n)
# print(long_to_bytes(m))