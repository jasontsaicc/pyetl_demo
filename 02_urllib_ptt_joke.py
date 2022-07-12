from urllib import request
import ssl

# 導入ssl模塊把證書驗證改成不用驗證
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.ptt.cc/bbs/joke/index.html"
# res = request.urlopen(url=url)

# 請求頭
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"}

req = request.Request(url=url, headers=headers)
res = request.urlopen(req)

print(res.read().decode('utf8'))
