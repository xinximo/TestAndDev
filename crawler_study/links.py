#!/usr/bin/python3
# @Time    : 2021/8/10 15:28
# @Author  : Wangx
import re
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
from config.log_config import Logger

'''
url 下载网址
pattern 正则化的匹配关键词
Directory 下载目录
'''
log = Logger(filename='./logs/app.log', level="info").logger


def BatchDownload(url, pattern):
    # 拉动请求，模拟成浏览器去访问网站->跳过反爬虫机制
    head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"
    }
    request = urllib.request.Request(url, headers=head)
    html = ''
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    soup = BeautifulSoup(html, "html.parser")
    data = []
    for item in soup.find_all('tr'):  # 查找符合要求的字符串
        item = str(item)
        link = re.findall(pattern, item)  # 通过正则表达式查找
        if len(link) > 0:
            data.append(url + link[0])
            log.info(f"开始下载:{url + link[0]}")
            urllib.request.urlretrieve(url + link[0], filename=f"./data/links/{link[0]}")


if __name__ == '__main__':
    pattern = re.compile(r'<a href="(Storm.*?)">')
    BatchDownload(url="https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/", pattern=pattern)
