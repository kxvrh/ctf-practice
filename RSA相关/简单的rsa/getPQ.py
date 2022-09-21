# 已知n, e, d, 求解p, q

import gmpy2
from Crypto.Util.number import *
import random

n = 0x73cec712124b33c0294e01eb52e8c3cd2fe9ddbcbf457b3b950360063dfae42cbbe9855bd986bcfea0948fadfb252f5e2ff3c982ff47afb6596a496636f1fc5ecfe9f5db7620b23fe9e30d230aa9299ab9a78bfb5e0630fd1149259b2b2104ea65d2e27b89785e4bf01d0594d9f94575cbcc3383f63c5aabe4d5b48eb761cce3ab21689b3f3155b5f15efee240d5ac149318ff80bd72a75fccdc57402aa197b472d98758019df8e9edb31bda82967dc66bcad845df824775eeb66ee304664d7929e8405122f9b0a5406887729dbe9760eb62dd7018087723c07c07082d1d51035fb211a9fc6d8fb5b3ee5bb91af5e3d0b89addce289041a5683a1fe7dc06a3bae283062ba3febdd987b5ac9b9a8ae4b8b02b804accc0a413bb144680fd8d0d8d8bebe176e5a9121f7653c31ede984d234ccce50e688f7048a0bfdfc84004c006ae912c4d4e514c200883e8dabaeb4bf57a5f628eb4bd2e6688d9b7688bc3eed4ce03831be5044dedbd5fddc43a3274b26c990a0e444fcf4a607de59c4906dfd1ea111920c38b4a365c5838e9cf1a22b146aa7afbc6e2e29ebe35aee4bf4d2fbe186c0f359c71f80b8f6298ad38619168d5986a857f558017c546d6df896c690896601aabd48398e957b77ef0e15d6cda339050b74cda3328c34c889306d089efc95ff467a4a775d3e104642cd9819f002b5db8c5f39b4e8d1a83007276b8a0b7
d = 0x37f2646fd190ad1e9f95c50d97cf4590a21e1c766bfd382cafafa2bb41442ce9839aac47944e288de6abfec1b17be4675f492a47f3e600f85a3823df9299d32f46c8a372f39d961f9471914e257f55cf1ef3d7878783fc34b61e1d61da332879c8d9597b0f0dac988916ac349e1d73b615cfbfef778ceeccee4f63dc32b1b7d7213c9199b6acb1d8a5141c94d777a29b89f8e0aea457788eaa9ca43626a24c74ebab355c89e3747626d4899745d148500c91416c782f2b30c9332f5cd32a4d3144d2a407ce9acc00f99dc619d425586285350cff734cdba9d4fad636d7fcbabfa382965005d8343e36ffe72604e557bae5044435ad990b6dca6d922e64387cee4abc0574d2eeeb42dda977be1e1064f6a6b00e78db75a7bf8e6e0c2ac3c6a52b2e6670cad3c907d990e53a7a311ef7b097c7644ff6f2bf96573e47d33031eeabf22620bdbc254a8fff8b0fa6f90d320c45e8d9094c26401f78560e16f77d6e09bc219c9849f1b68dc84ed36eb0cec7df16c4672c16a6b704ef2185ce04539f08688b72d48f9491e55be0095ee74f9622e8ae6835381e2efcd520cd02d1eeeb09bc11ab75bc903053102bc92718f2bf8691561a40026e53e950674f712aaef8cc69360df54c1af8b1f4aef997371b8a108e9b193a51002fe8d61f3991153e7ebd9593d68cd03b2f252c3d9d7a5bf802dcd150bd86028bd3b07cb415b767d716c1
e = 65537

k = e * d - 1

# method 1
# 参考https://www.di-mgt.com.au/rsa_factorize_n.html
# 选择一个随机数g, 1<g<n
# k为偶数, 所以k = r * 2^t, r为奇数且t >= 1
# 计算 x = g^(k/2), g^(k/4),...g^(k/2^t)
# 直到x > 1且y = gcd(x-1, n) > 1
# 若y存在, 则 p = y, q = n / y
# 若y不存在, 重新生成随机数g
p = 1
q = 1
while p == 1 and q == 1:
    k = e * d -1
    g = random.randint(0, n)
    while p == 1 and q == 1 and k % 2:
        k /= 2
        y = pow(g, k, n)
        if y != 1 and gmpy2.gcd(y-1, n) > 1:
            p = gmpy2.gcd(y-1, n)
            q = n / p
print(p)
print(q)


# method 2
# 由于n与z相差不大, 假设z和n位数相同
# e*d mod z = 1 --> e*d = h*z + 1  爆破出h, 求出z
# z = e * d - 1
# def cal_bit(num):
#     return len(bin(num)) - 2

# while z % 2 == 0:
#     z = z // 2
#     if cal_bit(z) == cal_bit(n):
#         print(z)
#         break

# n = p * q
# z = (p-1) * (q-1) = pq - (p+q) + 1
# p + q = n + 1 - z
# 因为任意实数a, b都可以写作 (X-a)*(X-b) = X^2 - (a+b)X + ab = 0的方程, 其解X1 = a, X2 = b
# 因此构造函数 X^2 - (p+q)X + pq = 1, 其解X1 = p, X2 = q
# 根据求根公式 X = [-b ± (根号下b方-4ac)] / 2a
# X1 = p = 1/2 * (p + q + 根号下(p+q)^2-4pq) = 1/2 * (n+1-z ± 根号下(n+1-z)^2 - 4n)
# X2 = q = 1/2 * (p + q - 根号下(p+q)^2-4pq)

# a = 1
# b = (n - z + 1)
# c = n
# p = (b + gmpy2.iroot(b**2 - 4*a*c)[0]) / 2
# q = n / p
# print(int(p))
# print(q)
