# affine仿射密码

# c = a*m + b(mod z)
# m = a^-1 * (c-b)(mod z)
# gcd(a,z)=1


alphabet_cipher = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# z = 26
# al = [1,3,5,7,9,11,15,17,19,21,23,25]
# bl = [x for x in range(0, 26)]

base32_cipher = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '2', '3', '4', '5', '6', '7']
# z = 32
# al = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]
# bl = [x for x in range(0, 32)]

def gcd(a, z=26):
    while z != 0:
        temp = a % z
        a = z
        z = temp
    return a

def encrypt(m, a, b, z=26):
    c = []
    for i in range(len(m)):
        # 小写字母加密成相应的大写字母 --> (26个字母的密码表)
        # ord:字符转ASCII, chr:ASCII转字符
        # ascii('a')=97, ascii('A')=65
        c.append(chr(((ord(m[i]) - 97) * a + b) % z +65))
    d = ''.join(c)
    print(d)

def decrypt(c, a, b, z=26):
    m = []
    k = reverse_a(int(a), z)
    print(k, b)

    for i in range(len(c)):
        if(ord(c[i]) >= 65 and ord(c[i]) <= 90):
            temp = ord(c[i]) - 65 - b
            if(temp < 0):
                temp += z
            m.append(base32_cipher[(k * temp) % z])
        elif(ord(c[i]) >= 48 and ord(c[i]) <= 57):
            temp = ord(c[i]) - 48 + 24 - b
            if(temp < 0):
                temp += z
            m.append(base32_cipher[(k * temp) % z])

        # if(ord(c[i]) >= 65 and ord(c[i]) <= 90):
        #     # 大写字母解码为小写字母
        #     temp = ord(c[i]) - 65 - b
        #     if temp < 0:
        #         temp += 26
        #     m.append(chr((k * temp) % z + 97))
        # elif(ord(c[i]) >= 48 and ord(c[i]) <= 57):
        #     # 数字
        #     temp = ord(c[i]) - 48 - b
        #     if temp < 0:
        #         temp += 10
        #     m.append(chr((k * temp) % z + 48))
        
    res = ''.join(m)
    print(res)
    
def reverse_a(a, z=26):
    # 求解a的乘法逆元
    ny = 1
    while (a * ny) % z != 1:
        ny += 1
    return ny

c = 'MZYVMIWLGBL7CIJOGJQVOA3IN5BLYC3NHI'

a = 13
b = 4
z = 32

decrypt(c,a,b,z)

# for i in range(0, 12):
#     for j in range(0, 26):
#         decrypt(c, al[i], bl[j])