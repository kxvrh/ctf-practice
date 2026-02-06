# rot13
# A B C D E F G H I J K L M
# N O P Q R S T U V W X Y Z

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
key =      ['A', 'X', 'J', 'H', 'G', 'T', 'D', 'S', 'Y', 'U', 'Z', 'I', 'R', 'C', 'V', 'B', 'P', 'M', 'F', 'N', 'W', 'Q', 'E', 'K', 'O', 'L']

n = 100
cyc = n % 26

c1 = 'XMVZGC RGC AMG RVMG HGFGMQYCD VT VWM BYNO, NSVWDS NSGO RAO XG UWFN AF '
c2 = 'HACDGMVWF. AIRVFN AII AMG JVRRVC-XVMC, FYRBIG TVIZ ESV SAH CGQGM XGGC '
c3 = 'RVMG NSAC A RYIG TMVR NSG SVWFG ESGMG NSGO EGMG XVMC WCNYI NSG HAO '
c4 = 'FVRG IVMH JARG MVWCH NV NAZG NSGR VTT NV EAM. OVWM TIAD YF "CV NSYF '
c5 = 'YF CVN JMOBNV RO HGAM", YC IVEGMJAFG, EYNS WCHGMFJVMGF YCFNGAH VT '
c6 = 'FBAJGF, FWMMVWCHGH XO NSG WFWAI "TIAD" NAD ACH JWMIO XMAJGF. GCUVO.'



def replace(c, key):
    m = []
    for i in range(len(c)):
        if(ord(c[i]) >= 65 and ord(c[i]) <= 90):
            temp = ord(c[i]) - 65
            m.append(key[temp])
        else:
            m.append(c[i])
    res = ''.join(m)
    print(res)

replace(c1, key)