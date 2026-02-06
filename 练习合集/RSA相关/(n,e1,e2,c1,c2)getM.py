# RSA共模
# 已知: n相同, 两组公钥e1,e2, c1,c2, 求m


# c1 = m^e1 mod n, c2 = m^e2 mod n
# 当e1,e2互质, 存在a*e1 + b*e2 = 1(其中a,b必为一正一负) --> 扩展欧几里得算法
# c1^a * c2^b mod n
# = ((m^e1 mod n)^a * (m^e2 mod n))^b mod n
# = m^(a*e1 + b*e2) mod n
# --> m = c1^a * c2^b

import gmpy2
import libnum

# 公钥解析获得相同的n和e1,e2
n = 
e1 = 
e2 = 

c1 = 
c2 = 

# 扩展欧几里得算法求a, b
s, s1, s2 = gmpy2.gcdext(e1, e2)

m = (pow(c1 ,s1, n) * pow(c2, s2, n)) % n
print(libnum.n2s(int(m)).decode())