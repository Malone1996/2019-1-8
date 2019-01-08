import json
import requests

while True:
    apikey = "7369ea076b1e457792215a68e12b9ba0"
    url = "http://openapi.tuling123.com/openapi/api/v2"
    json_params = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": input("请输入你想说的话:")
            },
        },
        "userInfo": {
            "apiKey": apikey,  # 换成自己的apikey
            "userId": "robot"  # 自定义一个名字即可
        }
    }
    content = requests.post(url, json=json_params).text
    content = json.loads(content)
    result = content.get("results")[0].get("values").get("text")
    print(result)
