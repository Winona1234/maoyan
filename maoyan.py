# -*- coding=utf-8 -*-
# @Time:2020/10/11 1:01 下午
# Author :王文娜
# @File:maoyan.py
# @Software:PyCharm
from urllib import request
import time
import re
import csv
import random
import pymysql
class maoyan(object):
    def __init__(self):
        self.url='https://maoyan.com/board/4?offset={}'
        self.ua_list=['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
        ,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0']
        self.page=1
        self.db=pymysql.connect(host='localhost',port=3306,user='root',password='',database='maoyan',charset='utf8')
        self.cursor=self.db.cursor()
    def get_page(self,url):
        headers={'user-agent':random.choice(self.ua_list)}
        req=request.Request(url=url,headers=headers)
        res=request.urlopen(req)
        html=res.read().decode('utf-8')
        self.parse_page(html)
    def parse_page(self,html):
        pattren = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>', re.S)
        # rlist: [('霸王别姬','张国荣','1993'),(),()]
        r_list = pattren.findall(html)
        self.write_page(r_list)

    # def write_page(self,r_list):
    #     with open('maoyan1.csv','a') as f:
    #         for rt in r_list:
    #             writer=csv.writer(f)
    #             writer.writerow([rt[0],rt[1].strip(),rt[2].strip()[5:15]])
    def write_page(self, r_list):
        # 定义空列表
        film_list = []
        ins = 'insert into ba(name,star,time) values(%s,%s,%s)'
        # 处理数据,放到大列表film_list中
        for rt in r_list:
            one_film = [
                rt[0], rt[1].strip(), rt[2].strip()[5:15]
            ]
            # 添加到大列表中
            film_list.append(one_film)
        # 一次数据库IO把1页数据存入
        self.cursor.executemany(ins, film_list)
        # 提交到数据库执行
        self.db.commit()
    def main(self):
        for offset in range(0,31,10):
            url=self.url.format(offset)
            self.get_page(url)
            time.sleep(random.randint(1,3))
        self.cursor.close()
        self.db.close()
if __name__=='__main__':
    start=time.time()
    spider=maoyan()
    spider.main()
    end=time.time()
    print('执行时间：%.2f'%(end-start))





