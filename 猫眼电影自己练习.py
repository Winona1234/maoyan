# -*- coding=utf-8 -*-
# @Time:2020/10/11 10:48 上午
# Author :王文娜
# @File:猫眼电影自己练习.py
# @Software:PyCharm
from urllib import request,parse
import re
import time
import random
class maoyan(object):
    def __init__(self):
        self.url='https://maoyan.com/board/4?offset={}'
        self.headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
    def get_page(self,url):
        req=request.Request(url=url,headers=self.headers)
        res=request.urlopen(req)
        html=res.read().decode('utf-8')
        return html
    def parse_page(self):
        pass
    def write_page(self,filename,html):
        with open(filename,'w') as f:
            f.write(html)
    def main(self):
        start = int(input('请输入起始页:'))
        end = int(input('请输入终止页:'))
        for page in range(start,end+1):
            offset=(page-1)*10
            url=self.url.format(offset)
            html=self.get_page(url)
            filename='{}页。html'.format(page)
            self.write_page(filename,html)
            print('{}页爬取成功'.format(page))
            time.sleep(random.randint(1,3))
if __name__=='__main__':
    spider=maoyan()
    spider.main()



