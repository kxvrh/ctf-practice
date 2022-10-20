import random
from hashlib import md5
# md5()只接受byte型参数: int.to_byte()或str.encode()

# 哈希碰撞
# version 1
for i in range(0, 100000):
    m = md5(str(i).encode())
    str1 = str(m.hexdigest())
    if '8b184b' == str1[-6:]:
        print(i)        # 53724

# version 2
res = '8b184b'
while 1:
    temp = random.randint(10**11, 10**12)
    temp = str(temp)
    MD5 = md5()
    MD5.update(temp.encode(encoding='utf-8'))
    flag = MD5.hexdigest()
    if flag[-6:] == res:
        print(temp)     # 261815215889
        break