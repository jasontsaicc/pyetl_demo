import requests
from bs4 import BeautifulSoup


url = "http://ec2-3-36-54-90.ap-northeast-2.compute.amazonaws.com/practice/123"

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

inputObjList = soup.select('input')
for i in inputObjList:
    print(i)

for i in inputObjList:
    if i['type'] == 'hidden':
        print(i['name'], i['value'])