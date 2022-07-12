import requests

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"
}

cookies = {
    "over18":"1"
}

res = requests.get(url, headers=headers, cookies=cookies )

print(res.text)