# 已知n, e, d, c以及p, q的高位
# 利用Coppersmith partial information attack求出new_p, new_q
# 高位已知攻击Factoring with high bits known Attack
# 仅需要知道p的log(2,new_n)/4比特数即可得到new_p

from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long, isPrime, getRandomNBitInteger
import binascii
import gmpy2

# n=0x241ac918f708fff645d3d6e24315e5bb045c02e788c2b7f74b2b83484ce9c0285b6c54d99e2a601a386237d666db2805175e7cc86a733a97aeaab63486133103e30c1dca09741819026bd3ea8d08746d1d38df63c025c1793bdc7e38d194a30b492aadf9e31a6c1240a65db49e061b48f1f2ae949ac9e7e0992ed24f9c01578d
# e=65537
# m=random.getrandbits(512)
# c=pow(m,e,n)=0x1922e7151c779d6bb554cba6a05858415e74739c36df0bcf169e49ef0e566a4353c51a306036970005f2321d1d104f91a673f40944e830619ed683d8f84eaf26e7a93c4abe1dbd7ca3babf3f4959def0e3d87f7818d54633a790fc74e9fed3c5b5456c21e3f425240f6217b0b14516cb59aa0ce74b83ca17d8cc4a0fbc829fb8
# ((p>>128)<<128)=0x2c1e75652df018588875c7ab60472abf26a234bc1bfc1b685888fb5ded29ab5b93f5105c1e9b46912368e626777a873200000000000000000000000000000000

n = 0x241ac918f708fff645d3d6e24315e5bb045c02e788c2b7f74b2b83484ce9c0285b6c54d99e2a601a386237d666db2805175e7cc86a733a97aeaab63486133103e30c1dca09741819026bd3ea8d08746d1d38df63c025c1793bdc7e38d194a30b492aadf9e31a6c1240a65db49e061b48f1f2ae949ac9e7e0992ed24f9c01578d
p_fake = 0x2c1e75652df018588875c7ab60472abf26a234bc1bfc1b685888fb5ded29ab5b93f5105c1e9b46912368e626777a873200000000000000000000000000000000

pbits = 1024
kbits = 130
pbar = p_fake & (2^pbits - 2^kbits)
print("upper %d bits (of %d bits) is given" % (pbits-kbits, pbits))


# 利用sage计算, 可使用在线网站 https://sagecell.sagemath.org/

# 生成一个以x为符号的多项式环, Zmod表示多项式系数类型
PR.<x> = PolynomialRing(Zmod(n))
#定义求解的函数
f = x + pbar
# find root < 2^kbits with factor >= n*0.3
# 多项式小值根求解, X表示求解根的上界
x0 = f.small_roots(X=2^kbits, beta=0.4)[0]
new_p = int(x0 + pbar)
print(hex(int(x0 + pbar)))