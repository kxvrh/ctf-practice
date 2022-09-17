import gmpy2
from Crypto.Util.number import long_to_bytes
import sympy

Bits = 512
e = 65537
n = 108525167048069618588175976867846563247592681279699764935868571805537995466244621039138584734968186962015154069834228913223982840558626369903697856981515674800664445719963249384904839446749699482532818680540192673814671582032905573381188420997231842144989027400106624744146739238687818312012920530048166672413
n = 108525167048069618588175976867846563247592681279699764935868571805537995466244621039138584734968186962015154069834228913223982840558626369903697856981515666845621033007989786615994090313753728974077390535576264003111280602310249175279283851900010535906485122009529323786354503926096748977474493688014416170407

gift = 9878713210057139023298389025767652308503013961919282440169053652488565206963320721234736480911437918373201299590078678742136736290349578719187645145615363088975706222696090029443619975380433122746296316430693294386663490221891787292112964989501856435389725149610724585156154688515007983846599924478524442938

c = 23970397560482326418544500895982564794681055333385186829686707802322923345863102521635786012870368948010933275558746273559080917607938457905967618777124428711098087525967347923209347190956512520350806766416108324895660243364661936801627882577951784569589707943966009295758316967368650512558923594173887431924

# temp = gmpy2.iroot(n, 2)[0]
# p = sympy.nextprime(temp)
# q = n // p
# print(p * q)


p,b1 = gmpy2.iroot(int((n*gift)/pow(10,631)),2)
print(b1)
p = sympy.nextprime(p)
q = n // p
print(gmpy2.is_prime(q))
print(p * q)


#q,b2 = gmpy2.iroot(int((n*gift)/pow(10,631)),2)
#print(b2)
# q = sympy.nextprime(q)
#print(p, q)


# tmp,b = gmpy2.iroot(n, 2)
# print(b)
# p = sympy.nextprime(tmp)
# while True:
# 	q = n // p
# 	q = sympy.nextprime(q)
# 	if(p*q == n):
# 		print(p)
# 		print(q)
# 		break
# 	p = sympy.nextprime(p)
# 	if(p / q > 0.99):
# 		break

z = (p-1) * (q-1)
d = gmpy2.invert(e, z)


m = gmpy2.powmod(c, d, n)
# print(long_to_bytes(m))