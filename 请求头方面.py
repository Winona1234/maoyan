# -*- coding=utf-8 -*-
# @Time:2020/10/12 10:41 上午
# Author :王文娜
# @File:请求头方面.py
# @Software:PyCharm
from urllib import request
import time
import re
import csv
import random
from useragents import ua_list
class maoyan(object):
    def __init__(self):
        self.url='https://maoyan.com/board/4?offset={}'
    def get_page(self,url):
        headers={'user-agent':random.choice(ua_list)}
        req=request.Request(url=url,headers=headers)
        res=request.urlopen(req)
        html=res.read().decode('utf-8')
        self.parse_page(html)
    def parse_page(self,html):
        pattren = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>', re.S)
        # rlist: [('霸王别姬','张国荣','1993'),(),()]
        r_list = pattren.findall(html)
        self.write_page(r_list)

    def write_page(self,r_list):
        one_film_dict={}
        for rt in r_list:
            one_film_dict['name'] = rt[0].strip()
            one_film_dict['star'] = rt[1].strip()
            one_film_dict['time'] = rt[2].strip()[5:15]
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
    print('执行时间：%.2f'%(end-start))