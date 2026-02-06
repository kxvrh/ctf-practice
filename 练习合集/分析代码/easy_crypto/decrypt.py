from Crypto.Util.number import bytes_to_long

with open('./enc.txt', 'rb')as f:
    flagx = f.read()

key = "hello world"

s = []
for i in range(0, 256):
    #s[i] = i
    s.append(i)

t = []
for i in range(0, 256):
    #t[i] = key[i % len(key)]
    t.append(key[i % len(key)])

j = 0
for i in range(0, 256):
    j = (j + s[i] + ord(t[i])) % 256
    tmp = s[i]
    s[i] = s[j]
    s[j] = tmp

flag = []
i = 0
j = 0
for m in range(0, 37):
    i = (i + 1) % 256
    j = (j + s[i]) % 256
    tmp = s[i]
    s[i] = s[j]
    s[j] = tmp
    x = (s[i] + (s[j] % 256)) % 256
    flag.append(flagx[m] ^ s[x])

print(flag)