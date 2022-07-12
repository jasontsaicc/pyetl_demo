import requests
from bs4 import BeautifulSoup
import ssl
import os

if not os.path.exists('./articles'):
    os.mkdir('./articles')

# 導入ssl模塊把證書驗證改成不用驗證
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.ptt.cc/bbs/movie/index.html"

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"}

for i in range(0, 1):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    titles = soup.select('div.title')
    # print(title)
    for title in titles:
        # print(title)

        # a-tag object <a href="/bbs/NBA/M.1656738748.A.640.html">[花邊] CYT-分析西區列強威脅程度 格林點名快艇獨行</a>
        titleObj = title.select_one('a')

        try:
            titleName = titleObj.text
            titleUrl = "https://www.ptt.cc/" + titleObj["href"]
            print(titleName)
            print(titleUrl)

            # Request titleUrl
            resArticle = requests.get(titleUrl, headers=headers)
            soupArticle = BeautifulSoup(resArticle.text, "html.parser")
            articleObj = soupArticle.select_one('div[id="main-content"]')
            articleStr = articleObj.text.split('※ 發信站:')[0]
            print(articleStr)
            try:
                with open('./articles/{}.txt'.format(titleName.replace("/", "")), "w", encoding='utf-8') as f:
                    f.write(articleStr)

            except OSError:
                pass

        except AttributeError as e:
            print(title)

        print("*" * 50)

    # lastPageUrl = "https://www.ptt.cc/" + soup.select('a[class="btn wide"]')[1]['href']
    lastPageUrl = "https://www.ptt.cc/" + soup.select('a.btn.wide')[1]['href']
    url = lastPageUrl
    # print(lastPageUrl)
