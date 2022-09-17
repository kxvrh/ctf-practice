# RSA共模
# 已知: n相同, 两组公钥e1,e2, c1,c2, 求m

import gmpy2
import libnum
from Crypto.Util.number import *

n1 = 13060424286033164731705267935214411273739909173486948413518022752305313862238166593214772698793487761875251030423516993519714215306808677724104692474199215119387725741906071553437840256786220484582884693286140537492541093086953005486704542435188521724013251087887351409946184501295224744819621937322469140771245380081663560150133162692174498642474588168444167533621259824640599530052827878558481036155222733986179487577693360697390152370901746112653758338456083440878726007229307830037808681050302990411238666727608253452573696904083133866093791985565118032742893247076947480766837941319251901579605233916076425572961
e1 = 117

# -----BEGIN PUBLIC KEY-----
# MIIBITANBgkqhkiG9w0BAQEFAAOCAQ4AMIIBCQKCAQBndV+JB5VkTsJ+aIkrlAQs
# eDNMNPmm2LaqSI2bQk1kqLmy3MkbHQmKCdesT5oGpLUmf4j4lotLrSkjXZqAMwhF
# 8Sa5qGX0THp333L3Y/VT6ZAgdF9AyNl/CrkGFU+7ECC1iPRB9xKyN3UFtkT+NqeH
# Q+5JlbQsexe430eC67WVCX7hvnQUMmGJPE7iwUDcRp4ysX+Ksw4l8HFkUGtOeca0
# 469b6gJoQn/7ETT7kKUSJynE7vF7bQsSz7pOfxTieqPCtPl451FjJC69XL1zgpM2
# +aEg6G4l1pyuAin9zOtbNdxjAYew7vFTLuxUb0A3puqw0CBxmblWYBGlL46azXJh
# AgMBAAE=
# -----END PUBLIC KEY-----

n2 = 13060424286033164731705267935214411273739909173486948413518022752305313862238166593214772698793487761875251030423516993519714215306808677724104692474199215119387725741906071553437840256786220484582884693286140537492541093086953005486704542435188521724013251087887351409946184501295224744819621937322469140771245380081663560150133162692174498642474588168444167533621259824640599530052827878558481036155222733986179487577693360697390152370901746112653758338456083440878726007229307830037808681050302990411238666727608253452573696904083133866093791985565118032742893247076947480766837941319251901579605233916076425572961
e2 = 65537


c1 = bytes_to_long(open(r'./cipher1.txt', 'rb').read())
c2 = bytes_to_long(open(r'./cipher2.txt', 'rb').read())
n = n1

# 扩展欧几里得算法求a, b
s, s1, s2 = gmpy2.gcdext(e1, e2)

m = (pow(c1 ,s1, n) * pow(c2, s2, n)) % n
print(libnum.n2s(int(m)).decode())
print(long_to_bytes(m))