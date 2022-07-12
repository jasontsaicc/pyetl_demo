import requests
import json

url = "https://buzzorange.com/techorange/wp/wp-admin/admin-ajax.php"

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"
}

dataStr = """action: ceris_posts_listing_grid
args[post_type]: post
args[ignore_sticky_posts]: 1
args[post_status]: publish
args[posts_per_page]: 8
args[offset]: 0
args[orderby]: date
postOffset: 8
type: loadmore
moduleInfo[post_source]: all
moduleInfo[post_icon]: disable
moduleInfo[iconPosition]: top-right
moduleInfo[post_icon_animation]: disable
moduleInfo[bookmark]: off
securityCheck: d8d887a36a
"""

data = {r.split(": ")[0]:r.split(": ")[1] for r in dataStr.split("\n")}
# print(data)

res = requests.post(url, headers=headers, data=data)

print(json.loads(res.text))
