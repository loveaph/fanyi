import requests
import json
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.98 Chrome/71.0.3578.98 Safari/537.36'}
url = 'https://fanyi.baidu.com/sug'
English = input('请输入查询的英语单词：')
data = {
    'kw': English

    }
response = requests.post(url=url,data=data,headers=headers)
text=response.json()
for i in text['data']:
    print('单词:%s\n翻译:%s\n'%tuple(i.values()))