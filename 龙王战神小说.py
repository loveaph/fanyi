import requests
from lxml import etree
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.98 Chrome/71.0.3578.98 Safari/537.36'}
url = 'http://book.zongheng.com/showchapter/1075540.html'
response = requests.get(url,headers).text
tree = etree.HTML(response)
page_all = tree.xpath('//ul[@class="chapter-list clearfix"]/li')
fp= open('./龙王战神.txt','w')
for page in page_all:
    page_url = page.xpath('./a/@href')[0]
    page_text = requests.get(page_url,headers).text
    tree = etree.HTML(page_text)
    title = tree.xpath('//div[@class="title_txtbox"]/text()')[0]
    text = tree.xpath('//div[@class="content"]//text()')[1:]
    fp.write(title+''.join(text))
    print(title,'下载成功')