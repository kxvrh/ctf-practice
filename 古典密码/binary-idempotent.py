# 二进制幂数加密法
# 26个字母 --> 2的0,1,2,3,4,5次幂就可以表示31个单元
# 例如第15个字母O 15 = 2^0 + 2^1 + 2^2 + 2^3 --> 0123





# c = '8842101220480224404014224202480122'
# 题目仅有1,2,4,8, 四个数字相加可以得到0-9任意数字
# 题目已知共8个大写字母, 密文中共7个0,将密文分割为8段,分别对应8个大写字母 --> 云影加密(以0分割)
# 即88421, 122, 48, 2244, 4, 142242, 248, 122
# 将数字相加得到对应字母序号, 如8+8+4+2+1 = 23
# 即 23, 5, 12, 12, 4, 15, 14, 5
# 即 W E L L D O N E
c = '8842101220480224404014224202480122'
enc = c.split('0')
num = []

def sum(list):
    sum = 0
    for i in list:
        for j in i:
            sum += int(j)
        num.append(sum)
        sum = 0
    return num
num = sum(enc)

def num2str(num):
    s = ''
    for i in num:
        s += chr(i+64)
    return s
print(num2str(num))