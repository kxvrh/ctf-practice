# 若e较小, 已知d的低位, 可求出完整的d
# Partial Key Exposure Attack部分私钥暴露攻击

# n = 0x51fb3416aa0d71a430157d7c9853602a758e15462e7c08827b04cd3220c427bbb8199ed4f5393dae43f013b68732a685defc17497f0912c886fa780dfacdfbb1461197d95a92a7a74ade874127a61411e14a901382ed3fb9d62c040c0dbaa374b5a4df06481a26da3fca271429ff10a4fc973b1c82553e3c1dd4f2f37dc24b3b
# e = 3  
# m = random.getrandbits(512)  
# c = pow(m,e,n)=0x3d7e16fd8b0b1afdb4e12594c3d8590f1175800ef07bb275d7a8ad983d0d5d5fd5c6f81efa40f5d10c48bb200f805e679d633ee584748e5feef003e0921dea736ba91eef72f3d591d3a54cd59fd36f61140fdd3fb2e2c028b684e50cbeae4a1f386f6ab35359d46a29996c0f7d9a4a189f1096150496746f064c3cc41cf111b0 
# d=invmod(e,(p-1)*(q-1))  
# d&((1<<512)-1)=0x17c4b18f1290b6a0886eaa7bf426485a3994c5b71186fe84d5138e18de7e060db57f9580381a917fdfd171bfd159825a7d1e2800e2774f5e4449d17e6723749b

# 需要运行sage https://sagecell.sagemath.org/

def partial_p(p0, kbits, n):
    # d0表示已知的d的低位  
    # kbits为已知的d0的位数
    PR.<x> = PolynomialRing(Zmod(n))  
    nbits = n.nbits()  
    f = 2^kbits*x + p0  
    f = f.monic()  
    roots = f.small_roots(X=2^(nbits//2-kbits), beta=0.3)  # find root < 2^(nbits//2-kbits) with factor >= n^0.3  
    if roots:  
        x0 = roots[0]  
        p = gcd(2^kbits*x0 + p0, n)  
        return ZZ(p)  
  
  
def find_p(d0, kbits, e, n):  
    X = var('X')  
  
  
    for k in range(1, e+1):  
        results = solve_mod([e*d0*X - k*X*(n-X+1) + k*n == X], 2^kbits)  
        for x in results:  
            p0 = ZZ(x[0])  
            p = partial_p(p0, kbits, n)  
            if p:  
                return p  

# n --> 必须为整形才可计算, 转为十进制
# d0=给出的部分d --> 必须为整形才可计算,转为十进制
e = 3
n = 57569201048993475052349187244752169754165154575782760003851777813767048953051839288528137121670999884309849815765999616346303792471518639080697166767644957046582385785721102370288806038187956032505761532789716009522131450217010629338000241936036185205038814391205848232364006349213836317806903032515194407739
nbits = n.nbits()
kbits = floor(nbits*0.5)
print ("kbits : ", kbits)
d0 = 1244848677959253796774387650148978357579294769878147704641867595620534030329181934099194560059806799908134954814673426128260540575360296026444649631806619
print ("lower %d bits (of %d bits) is given" % (kbits, nbits))

p = find_p(d0, kbits, e, n)
print ("found p: %d" % p)
q = n//p
# print d
print ("完整的d是:"+str(inverse_mod(e, (p-1))))