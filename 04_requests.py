from urllib import request
from bs4 import BeautifulSoup
import ssl

# 導入ssl模塊把證書驗證改成不用驗證
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.ptt.cc/bbs/joke/index.html"
# res = request.urlopen(url=url)

# 請求頭
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"}

# req = request.Request(url=url, headers=headers)
# res = request.urlopen(req)

# print(res.read().decode('utf8'))
# “b”開頭代表其型態為bytes 使用decode(‘utf8’) 將 bytes轉為字串
# htmlStr = res.read().decode('utf8')

htmlStr = request.get(url, headers=headers).text
soup = BeautifulSoup(htmlStr, 'html.parser')
# print(soup)

# print(soup.findAll('a', {'id':'logo'}))

a_logo_tag_list = soup.findAll('a', id='logo')  # list

# print(a_logo_tag_list[0])  # tag object
# # 取出裡面的文字 加.text
# print(a_logo_tag_list[0].text)  # string object
#
# # get specific attribute value
# print("https://www.ptt.cc" + a_logo_tag_list[0]['href'])

# #### select###
# a_board_tags = soup.select('a[class="board"]')
# # 對外層標籤 在進行一次select
# print(a_board_tags)
# print(a_board_tags[0].select('span'))
# print(a_board_tags[0].select('span.board-label'))
# print(a_board_tags[0].find('span'))
#
# print(type(soup))
# print(type(a_board_tags[0]))

