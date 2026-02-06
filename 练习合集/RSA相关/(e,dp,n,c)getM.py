# RSA
# 已知e,dp,n,c
# dp = d mod (p-1)

# e * d = 1 mod ((p - 1)*(q - 1))   --> e * d = k0 + (p - 1)*(q - 1)
# dp = d mod(p - 1)                 --> e * dp = e * d mod(p-1)
# e * d  = k1 * (p - 1)*(q - 1) + 1 = k1 * (e * d - k0) + 1
#        = k2 * (p - 1) + e * dp
# e * dp = (p - 1) * (k1 * (q - 1) - k2) + 1
# 因为dp < p, 所以 e > k1*(q - 1) - k2 ∈ (1, e)
# 遍历即可得p值

import gmpy2
from Crypto.Util.number import long_to_bytes
e = 
dp = 
n = 
c = 

for p in range(1, e):
    if(e* dp - 1)% p == 0 and n %((e*dp-1)//p+1)==0:
        q = n //((e*dp-1)//p+1)
        z = (q - 1) * ((e*dp -1)//p)
        d = gmpy2.invert(e, z)
        m = gmpy2.powmod(c, d, n)

print(long_to_bytes(m))