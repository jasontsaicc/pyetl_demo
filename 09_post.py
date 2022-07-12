import requests


# url = "http://httpbin.org/post"
url = "http://ec2-3-36-54-90.ap-northeast-2.compute.amazonaws.com/hello_post"

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"}

data = {
    "key1":"value1",
    "key2":"value2",
    "username":"fsderawDWD"
}

res = requests.post(url, headers=headers, data=data)

print(res.text)