import json
import requests
import cloudscraper
import pprint
import os

if not os.path.exists("./dcard"):
    os.mkdir("./dcard")

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36'
}
# headers = {
#     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"
# }
#
# url = "https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=30&before=239238602"

# res = requests.get(url, headers=headers)

# ss = requests.Session()
# ss.headers = headers
#
# scraper = cloudscraper.create_scraper(sess=ss)
# res = scraper.get(url)
#
# print(res.text)
#
with open('./dcard.json', 'r', encoding='utf-8') as f:
    jsonDate = json.loads(f.read())
# for obj in jsonDate:
#     print(obj)
# print(jsonDate[1].keys())
pprint.pprint(jsonDate[0])

"""
'mediaMeta': [{'createdAt': '2022-06-30T13:42:17.286Z',
                'height': 1322,
                'id': '46ee8e01-01dc-4dc3-ac01-a0f07cb8c2c2',
                'normalizedUrl': 'https://i.imgur.com/svHPDsYl.jpg',
                'tags': ['ANNOTATED'],
                'thumbnail': 'https://i.imgur.com/svHPDsYl.jpg',
                'type': 'image/thumbnail',
                'updatedAt': '2022-06-30T13:42:17.286Z',
                'url': 'https://i.imgur.com/svHPDsYl.jpg',
                'width': 2000},
"""
for articleObj in jsonDate:
    title = articleObj['title']
    articleUrl = "https://www.dcard.tw/f/photography/p/" + str(articleObj['id'])
    print(title)
    print(articleUrl)

    for idx, imgObj in enumerate(articleObj['mediaMeta']):
        imgUrl = imgObj['url']
        print("\t", imgUrl)
        imgRes = requests.get(imgUrl, headers=headers)
        try:
            with open('./dcard/{}_{}.jpg'.format(title.replace("/", ""), idx), 'wb') as f:
                f.write(imgRes.content)
        except OSError:
            pass

    print("========")