from Crypto.Util.number import bytes_to_long

key = "hello world"

s = []
for i in range(0, 256):
    s[i] = i

t = []
for i in range(0, 256):
    t[i] = key[i % len(key)]

j = 0
for i in range(0, 256):
    j = (j + s[i] + t[i]) % 256
    tmp = s[i]
    s[i] = s[j]
    s[j] = tmp

with open('./flag.txt', 'rb')as f:
    content = f.read()
    flag = bytes_to_long(content)

flagx = []
for m in range(0, 37):
    i = (i + 1) % 256
    j = (j + s[i]) % 256
    tmp = s[i]
    s[i] = s[j]
    s[j] = tmp
    x = (s[i] + (s[j] % 256)) % 256
    flagx[m] = flag[m] ^ s[x]

print(flagx)