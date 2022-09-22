# RSA已知n, 密文c, 公钥e, 求明文

import gmpy2
from Crypto.Util.number import long_to_bytes, bytes_to_long
import base64

# 通过公钥解析得到n, e
e = 9850747023606211927
n = 62078208638445817213739226854534031566665495569130972218813975279479576033261

# 通过分解n得到p, q
### 注意!!!p,q的顺序很重要!!!
q = 184333227921154992916659782580114145999
p = 336771668019607304680919844592337860739

# 观察flag.enc 中的数据很大
# 说明初始的n并不能作为最后加密的N值
# 因为RSA加密需要公钥n的长度至少是大于消息的长度的, 否则加密出来的密文会无法解密


with open('./flag.enc','rb')as f:
    # 密文c
    b64_c = f.read()
c = bytes_to_long(base64.b64decode(b64_c))

i = 1
while 1:
    print(i)
    print(p)
    print(q)
    print(e)
    i += 1
    n = p*q
    if(n >= c):                 # n的长度要至少大于消息的长度
        
        z = (p-1) * (q-1)
        d = gmpy2.invert(e, z)
        m = gmpy2.powmod(c, d, n)
        print(long_to_bytes(m))
        break
    else:
        p = gmpy2.next_prime(p**2 + q**2)
        q = gmpy2.next_prime(2*q*p)
        e = gmpy2.next_prime(e**2)
        # 加密时try...except...的内容

# p = 102976639096844807764310074758387731794509878311969352166703955480673284271854714461014587360939592213426236482760461269444083625335562318999973299123493634458124910479617050885641619377365226613676095388730193278734980007335766341801229373414010772190044892509566499891628107926903113498199991661062142493155082683224656395881576458415540724968047113369402985851101538104307131321298412547008605045461918803884405371571243776355892091640394261717442621108816102952631226814031390522797722671211829631558354849113042066597195368960787932181501727531813031671959970650550200759732071942726650719116715140258769202512977531331573085264105597367942429940889807555435534393766721883604734076625570333
# q = 66090352129600760449660103036348852620295365702546350540439935352095492183997479438835275332736028050279535562592752053328311440343036150090710687840307864839678876978834154180880593361904306407592157603263757053769474544190282070783372536625552621057988751575360534579130800416749730892561290398995360907094366871114159728985005399292513022396518392323447383830396682967815871211470632074996488908880228478986732494474259304760321793625041677177862764173893824364658760699180881698766222753433298466452688140821441136736986437637034212983477601827328247113625498277330727486282477874233425576708207016980845970181202949357926396835387253991488295035916129522894012151738505813199808787854548091699894040746559332256963163672278374455635148454197744916000403717495759936149390391782639207639444307488763095809558476841795125128144704210076047508028569685073777640192535046026650368462016343949971502399652048792874435560535166084733582216812020295191471462889520461317816708026777119521654910378738198881408219051789155728273655838986558649139
# e = 88665226737779504449341190616137151988381490336612521631987290031713639310361743831757596667941482184295653578954177433875698775138134067682697183623423

# e = 88665226737779504449341190616137151988381490336612521631987290031713639310361743831757596667941482184295653578954177433875698775138134067682697183623423