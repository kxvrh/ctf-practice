# 当n很大且p, q很接近时
import gmpy2

n = 108525167048069618588175976867846563247592681279699764935868571805537995466244621039138584734968186962015154069834228913223982840558626369903697856981515674800664445719963249384904839446749699482532818680540192673814671582032905573381188420997231842144989027400106624744146739238687818312012920530048166672413
a = gmpy2.iroot(n, 2)[0]

# # method 1
# while 1:
#     B2 = pow(a, 2) - n
#     a += 1
#     if gmpy2.is_square(B2):
#         b = gmpy2.iroot(B2, 2)[0]
#         p1 = a + b
#         q1 = a - b
#         print(p1)
#         print(q1)
#         break

# method 2
p2 = gmpy2.next_prime(a)
q2 = n // p2
print(p2)
print(q2)
