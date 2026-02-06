import random
from string import ascii_letters, digits, punctuation
from itertools import permutations
from hashlib import md5
from sys import prefix
# md5()只接受byte型参数: int.to_byte()或str.encode()

# 哈希碰撞尾数
# version 1
def decrypt_md5_res1(res):
    for i in range(0, 100000):
        m = md5(str(i).encode())
        str1 = str(m.hexdigest())
        if res == str1[-6:]:
            print(i)        # 53724

# version 2
def decrypt_md5_res2(res):
    while 1:
        temp = random.randint(10**11, 10**12)
        temp = str(temp)
        MD5 = md5()
        MD5.update(temp.encode(encoding='utf-8'))
        flag = MD5.hexdigest()
        if flag[-6:] == res:
            print(temp)     # 261815215889
            break


all_letters = digits + ascii_letters + punctuation + '.,;'

def decrypt_md5(md5_value, prefix, k):
    if len(md5_value) != 32:
        print('invalid md5 value!')
        return
    md5_value = md5_value.lower()
    for iter in range(1, k):
        print('Iterating: %d' %iter)
        for item in permutations(all_letters, iter):   # 全排列
            item = ''.join(item)
            string = prefix + item
            if md5(string.encode()).hexdigest().lower() == md5_value:
                print('found!!: %s' % item)
                return
    print('Not found...try a bigger k.')

def online_decrypt_md5(md5hash):
    apikey='83750c877f8523955b3e0204'
    rtype = 'crack'
    url = 'http://api.md5crack.com/'+rtype+'/'+apikey+'/'+md5hash
    r = requests.get(url)
    print (r.json())

if __name__ == '__main__':
    res = '8b184b'
    # decrypt_md5_res1(res)
    # decrypt_md5_res2(res)
    
    md5_value = 'a6f57ae38a22448c2f07f3f95f49c84e'
    prefix = 'ctfshow'
    decrypt_md5(md5_value, prefix, 5)
