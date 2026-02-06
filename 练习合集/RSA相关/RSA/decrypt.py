#!/usr/bin/env python2.7
from gmpy import *
from Crypto.Util.number import getPrime
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from base64 import b64decode

flag_encode=b64decode(open('flag.enc','r').read())
pub=RSA.importKey(open('pubkey.pem','r').read())
n=pub.n
e=pub.e

# use http://www.factordb.com to decomposition factor
q=184333227921154992916659782580114145999
p=336771668019607304680919844592337860739
i=1
while 1:
        print(i)
        print(p)
        print(q)
        print(e)
        i+=1
        n=q*p
        if n >= int(flag_encode.encode('hex'),16):
                fn=(p-1)*(q-1)
                d=invert(e,fn)
                prikey=RSA.construct((int(n),int(e),int(d)))
                key=PKCS1_v1_5.new(prikey)
                dec=key.decrypt(flag_encode,None)
                break
        else:
                p=next_prime(p**2+q**2)
                q=next_prime(2*q*p)
                e=next_prime(e**2)

print (dec)