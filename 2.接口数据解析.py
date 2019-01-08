# 接口,API
# 接口数据格式:xml(基本不存在)/json(普遍)

import requests

url = "http://api.map.baidu.com/telematics/v3/weather?location=郑州市&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?"
content = requests.get(url).text
# print(content)

# json和字典的关系
# 如果把字典转换成字符串,就是json

import json

# json字符串 转 字典
tian_qi = json.loads(content)
# print(tian_qi)

print('天气预报:')
print(
    '---------------------------------------------------------------------------------------------------------------------------------------------------------')
today = tian_qi.get('results')[0].get('weather_data')[0]  # 提取所需数据
pm25 = tian_qi.get('results')[0].get('pm25')
index = tian_qi.get('results')[0].get('index')[0]

print(f"当前的日期为:{today.get('date')}")
print(f"当前的PM2.5为:{pm25}")
print(f"当前的天气为:{today.get('weather')}")
print(f"当前的风速为:{today.get('wind')}")
print(f"当前的温度为:{today.get('temperature')}")
print(f"当前天气状况为:{index.get('zs')}")
print(f"穿衣建议为:{index.get('des')}")

print(
    '---------------------------------------------------------------------------------------------------------------------------------------------------------')

# 字典 转 json字符串
# 如果字典中有汉字,转换时可能会有乱码,最好设置ensure_ascii=False
json_str = json.dumps(tian_qi, ensure_ascii=False)
# print(json_str)
