import re
import requests
from lxml import etree


def url_download(url):
    res = requests.get(url)
    res.encoding = 'gbk'
    return res.text


def parse_url(text):
    file = r'D:\学习\编程\练习\2022\20220712-爬取道德经网页\道德经.txt'
    se = etree.HTML(text)
    txt = se.xpath('//div[@class="STYLE4"]/p/text()')
    with open(file,'w',encoding='utf8') as f:
        for t in txt:
            content1 = "".join(re.findall('[^〖〗]',t))
            content = re.sub('【','\n【',content1.strip())
            f.write(content)


if __name__ == '__main__':
    url = 'https://www.daodejing.org/'
    resp = url_download(url)
    parse_url(resp)