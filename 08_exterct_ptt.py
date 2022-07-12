import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/movie/M.1656663806.A.0D7.html"

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

articleObj = soup.select_one('div[id="main-content"]')
# print(articleObj)
for div in articleObj.select('div'):
    # print(div)
    div.extract()
print(articleObj)