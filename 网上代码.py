# -*- coding=utf-8 -*-
# @Time:2020/10/11 8:40 下午
# Author :王文娜
# @File:网上代码.py
# @Software:PyCharm
import time
import re
from urllib import request,parse
import random

class maoyan(object):

    def __init__(self):
        self.url='https://maoyan.com/board/4?offset=0'
        self.ua_list=['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0']
    def get_page(self,url):
        headers = {'User-agent': random.choice(self.ua_list)}
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')


    def parse_page(self,html):
        pattern = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>'.re.S)
        r_list = pattern.findall(html)
        self.parse_page(html)
        self.write_page(r_list)
    def write_page(self,r_list):
        one_film_dict={}
        for rt in r_list:
            one_film_dict['name']=rt[0].strip()
            one_film_dict['star'] = rt[1].strip()
            one_film_dict['time'] = rt[2].strip()
            print(one_film_dict)
    def main(self):
        for offset in range(0,91,10):
            url=self.url.format(offset)
            self.get_page(url)
            time.sleep(random.randint(1,3))






if __name__=='__main__':
    start=time.time()
    spider=maoyan()
    spider.main()
    end=time.time()
    print('程序等等执行时间为:%.2f'%(end-start))


