# -*- coding=utf-8 -*-
# @Time:2020/10/11 8:07 上午
# Author :王文娜
# @File:百度贴吧1.py
# @Software:PyCharm
from urllib import request,parse
import time
import random
class BaiduSpider(object):
    def __init__(self):
        self.url='https://tieba.baidu.com/f?kw={}&pn={}'
        self.headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

        pass
    def get_page(self,url):
        req=request.Request(url=url,headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        return html

    def write_page(self,filename,html):
        with open(filename,'w') as f:
            f.write(html)

    def main(self):
        name=input('请输入贴吧名')
        start=int(input('请输入起始页'))
        end = int(input('请输入终止页'))
        for page in range(start,end+1):
            pn=(page-1)*50
            kw=parse.quote(name)
            url=self.url.format(kw,pn)
            html=self.get_page(url)
            filename='{}-第{}页.html'.format(name,page)
            self.write_page(filename,html)
            print('第{}页爬取成功'.format(page))
            time.sleep(random.randint(1,3))

if __name__=='__main__':
    spider=BaiduSpider()
    spider.main()



