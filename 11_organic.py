import requests
from bs4 import BeautifulSoup

url = "https://organic.afa.gov.tw/InOrganic/QueryApplyList"

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"}
data = {
    "TYPE": "1",
    "YEAR": "111",
    "qNnify_NO": "",
    "qC_NAME": "",
    "qPaper_NO": "",
    "qProduct_NAME": "米".encode("big5"),
    "B": "查　　詢"
}

headersStr = """Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-CN;q=0.5
Cache-Control: max-age=0
Connection: keep-alive
Content-Length: 91
Content-Type: application/x-www-form-urlencoded
Cookie: JSESSIONID=1A6120A9CDCE2D0ACE0AE04F9C15B31E; TS018193af=010df39fec4f90ff735d7d764d8e62d2ac8cd231db88ed89ec925eb0cab52a72d03819a79d7d094bedfe923676d0ffc10ff3e92071ea9788f0e4b9462d3886f001edc51347; TS01bc7d78=010df39fec1bc2c55c6af7fb486c426f6a57abdd7abfe4281ccec52ffe711c4e5b160ad96df9b6dbea0743cd4fb25584c92f104c8f
Host: organic.afa.gov.tw
Origin: https://organic.afa.gov.tw
Referer: https://organic.afa.gov.tw/InOrganic/QueryApplyList?TYPE=5
sec-ch-ua: " Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "macOS"
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"""

res = requests.post(url, headers=headers, data=data)
print(res.text)

headers = {r.split(": ")[0]:r.split(": ")[1] for r in headersStr.split("\n")}
print(headers)
