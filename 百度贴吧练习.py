# -*- coding=utf-8 -*-
# @Time:2020/10/11 10:25 上午
# Author :王文娜
# @File:百度贴吧练习.py
# @Software:PyCharm
import re
from urllib import request,parse
import time
import random
class baiduspider(object):
    def __init__(self):
        self.url='https://tieba.baidu.com/f?kw={}&pn={}'
        self.headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
    def get_page(self,url):
        req=request.Request(url=url,headers=self.headers)
        res=request.urlopen(req)
        html=res.read().decode('utf-8')
        return html
    def parse_page(self,html):
        pass
    def write_page(self,filename,html):
        with open(filename,'w') as f:
            f.write(html)
    def main(self):
        name=input('请输入贴吧名')
        start=int(input('请输入开始页码'))
        end=int(input('请输入终止页码'))
        for page in range(start,end+1):
            pn = (page - 1) * 50
            kw=parse.quote(name)
            url=self.url.format(kw,pn)
            html=self.get_page(url)
            filename='{}-第{}页爬取成功'.format(name,page)
            self.write_page(filename,html)
            print('第{}页爬取成功'.format(page))
            time.sleep(random.randint(1,3))
if __name__=='__main__':
    spider=baiduspider()
    spider.main()



