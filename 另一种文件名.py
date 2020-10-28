# -*- coding=utf-8 -*-
# @Time:2020/10/11 12:18 下午
# Author :王文娜
# @File:另一种文件名.py
# @Software:PyCharm
import csv

with open('test.csv','w',newline='') as f:
    # 初始化写入对象
    writer = csv.writer(f)
    writer.writerow(['超哥哥',20])
    writer.writerow(['步惊云', 22])
with open('test.csv','a',newline='') as f:
    writer=csv.writer(f)

    writer.writerows([('小',67),('大',90)])
