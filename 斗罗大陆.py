from bs4 import BeautifulSoup
import requests
import time
import random
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.98 Chrome/71.0.3578.98 Safari/537.36'}
url = ('http://www.zmccx.com/54_54196/')
response = requests.get(url,headers).content
soup = BeautifulSoup(response,'lxml')
title_all = soup.find_all('div',id="list")[0].find_all("dd")
fp = open('./斗罗大陆.txt','w')
for dd in title_all:
    title = dd.a.text
#    print(dd)
    time.sleep(random.randint(1,4))
    page_url = 'http://www.zmccx.com'+dd.a['href']
#    print(page_url)
    page_text = requests.get(page_url,headers).content
    soup = BeautifulSoup(page_text,'lxml')
    page = soup.find('div',id="content").text     #属性选择器
#    page = soup.select('#content')      #类选择器
#    print(page)
    fp.write(title+page)
    print(title,'下载成功！！！！！！！')


        