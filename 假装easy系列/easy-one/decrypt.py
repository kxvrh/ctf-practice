# 线性加密
# c = (p + (k[i % strlen(k)] ^ t) + i*i) & 0xff
# 0xff取变量前二进制8位, 按位与1, 当变量为正数时不变, 当变量为负数, 符号位改变
# k[i % strlen(k)]即k的每一位循环加密
# msg001 --> msg001.enc, flag --> msg002.enc
# python2打开 (python3 ord()报错)

def openfile(filename, method='rb+'):
    with open(filename, method)as f:
        content = f.read()
        result = [ord(x) for x in content]
    f.close()
    return result

plaintext = openfile("msg001")
cipher = openfile("msg001.enc")


key = ""
t = 0
for i in range(len(plaintext)):
    # c = (p + (k[i % strlen(k)] ^ t) + i*i) & 0xff
    k = ((cipher[i] - plaintext[i] - i*i) ^ t) & 0xff
    t = plaintext[i]
    key += chr(k)
# print(key)
# VeryLongKeyYouWillNeverGuessVe
key = "VeryLongKeyYouWillNeverGuess"

enc = openfile("msg002.enc")

flag = ""
t = 0
for i in range(len(enc)):
    p = (enc[i] - (key[i%len(key)]^t) - i*i) & 0xff
    t = p[i]
    flag += chr(p)
print(flag)

# The known-plaintext attack (KPA) is an attack model for cryptanalysis where the attacker has samples of both the plaintext (called a crib), and its encrypted version (ciphertext). These can be used to reveal further secret information such as secret keys and code books. The term "crib" originated at Bletchley Park, the British World War II decryption operation. 
# The flag is CTF{6d5eba48508efb13dc87220879306619}
