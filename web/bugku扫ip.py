from urllib import request
import urllib3
import requests

headers = {
"Cache-Control": "max-age=0",
"Upgrade-Insecure-Requests":'1',
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Connection": "close"
}

# r=requests.get('http://192-168-1-118.pvp1237.bugku.cn/',headers=headers)
# print(r.content)


url='http://192-168-1-{}.pvp1560.bugku.cn/'
for i in range(1,255):
    url1=url.format(str(i))
    try:
        r=requests.get(url1,headers=headers)
        if len(r.content)>200:
            print(url1)
    except:
        pass
    
    
