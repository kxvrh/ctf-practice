# RSA
# 已知p,q,dp,dq,c

# dp ≡ d mod (p-1)          --> d = dp + k1 * (p - 1)
# dq ≡ d mod (q-1)          --> d = dq + k2 * (q - 1)
# m = c^d mod n
# m1 ≡ c^d mod p            --> c^d = k * p + m1        --> m1 = c^(dp mod(p - 1)) mod p    --> m1 = c^dp mod p
# m2 ≡ c^d mod q                                        --> m2 = c^(dq mod(q - 1)) mod q    --> m2 = c^dq mod q (费马小定理)
#    = (k * p + m1) mod q   
# 两边同时减去m1得  --> (m2 - m1) ≡ k * p mod q
# 因为 gcd(p, q) = 1, 可求得p的逆元p^-1
# p^-1 * (m1 - m2) ≡ k mod q
# k = p^-1 * (m1 - m2) mod q
# c^d = (p^-1 * (m1 - m2) mod q) * p + m1
# m = ((p^-1 * (m1 - m2) mod q) * p + m1)mod n
# m1 = c^d mod p
#    = c^(dp + k*(p - 1))mod p
#    = c^dp * c^(k * (p-1))mod p
#由费马小定理
# c^(k * (p-1))mod p = (c^(p -1) mod p)^k = 1^k = 1
# 所以
# m1 = c^dp mod p, m2 = c^dq mod q 
# 故 m ≡ c^d = (p^-1 * (m1 - m2) mod q) * p + m1

import gmpy2
from Crypto.Util.number import long_to_bytes

p = 
q = 
dp = 
dq = 
c = 

m1 = gmpy2.powmod(c, dp, p)
m2 = gmpy2.powmod(c, dq ,q)
I = gmpy2.invert(p, q)
m = (((m1 - m2) * I) % q)*p + m1
print(long_to_bytes(m))