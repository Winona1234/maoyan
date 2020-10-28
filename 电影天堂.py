# -*- coding=utf-8 -*-
# @Time:2020/10/12 3:49 下午
# Author :王文娜
# @File:电影天堂.py
# @Software:PyCharm
from urllib import request
import re
import random
import time
from useragents import ua_list
class filmsky(object):
    def __init__(self):
        self.url='https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'


    def get_page(self,url):
        headers={'User-Agent':random.choice(ua_list)}
        req=request.Request(url=url,headers=headers)
        res=request.urlopen(req)
        html=res.read().decode('gbk','ignore')
        return html
    def parse_page(self,html):
        pattern=re.compile('<table width="100%".*?<td height="26">.*?<a href="(.*?)".*?>(.*?)</a>',re.S)
        film_list=pattern.findall(html)
        for film in film_list:
            film_name=film[1]
            film_link='https://www.dytt8.net'+film[0]
            download_link=self.parse_two_html(film_link)
            d={'电影名称':film_name,'下载连接':download_link}
            print(d)
    def parse_two_html(self,film_link):
        two_html=self.get_page(film_link)
        pattern=re.compile('<td style="WORD-WRAP.*?>.*?>(.*?)</a>',re.S)
        download_link=pattern.findall(two_html)[0]
        return download_link

    def main(self):
        for page in range(1,3):
            url=self.url.format(page)
            html=self.get_page(url)
            self.parse_page(html)
            time.sleep(random.randint(1,3))

if __name__=='__main__':
    start=time.time()
    spider=filmsky()
    spider.main()
    end=time.time()
    print('执行时间：%.2f'%(end-start))



