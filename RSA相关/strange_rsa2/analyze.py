# from Crypto.Util.number import *

# def generate_poly(p, Bits, a):
#     poly = []
#     res = 0
#     for i in range(1, Bits+1):                    --> 循环Bits次
#         poly.append(getRandomRange(1, p-1))       --> poly加上[1, p-1)中一随机数x
#         res = (res + poly[-1] * pow(a, i, p)) % p --> res = (res + x * a^i mod p) % p
#                                                   --> Ri+1 = (Ri + poly[i-1] * (a^i mod p)) % p
#                                                   --> Ri = Σ(poly[i-1] * a^i) % p                 i >= 1
#     return [p-res] + poly                         --> p - R512 , poly[0, 512]
    
# Bits = 4
# p = getPrime(Bits)
# print(p)
# a = getRandomRange(1, p-1)
# print(a)

# k = 2
# s1 = generate_poly(p, Bits, a)                    --> g1 = p - Σ(poly1[i-1] * a^i) % p              i = 512
# s2 = generate_poly(p, Bits, a * k)                --> g2 = p - Σ(poly2[i-1] * ak^i) % p
#                                                   --> g1 - g2 = Σ(poly2[i-1]*k^i - poly1[i-1]) a^i

a = 1
k = 1
g1 = 5427094460745472513593814790243139230026320357992492902728810995081053349454308946008416635445657899000855266472167839129495101472281709819578765877508334
g2 = 4279087087206631299154411600466833621745324873794665428463889581772246205318703604503913091125412611067658249454600222710553516195589206172844202542978787
res = g1 - g2

while(len(str(a)) <= 47):
    sum = 0
    for i in range(1, 513):
        sum = sum + (poly2[i-1] * pow(k, i) - poly1[i-1]) * pow(a, i)
    if sum == res:
        print(k)
        print(a)



# Bits = 512, p = getPrime(Bits)    --> p < 2^512 - 1
# poly和(g = p - res)都是154个比特位, 0 < poly < p  --> p和res均为154个比特位   --> 2^154共47个数字
import sympy
import gmpy2

n = 109378672508048135963067490399488700128935926221280999153728844885929604845257426753717908439401874480024019118872754964261258108802571658255339464890951241819976505839994513576969957522261002976457875212789578122239936311323485029004004912939615422858758136864345993327406831607042382680866135088327787314829
p = pow(2, 154)
while(len(str(p)) == 47):
    p = sympy.nextprime()
    q = n // p
    if(p*q == n):
        print(p)
        print(q)
        break

        

