# -*- coding=utf-8 -*-
# @Time:2020/10/13 11:03 上午
# Author :王文娜
# @File:zhaoliying.py
# @Software:PyCharm
import requests
url='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1602567982966&di=ee3ac83a7c005e3cfe0f6f97e1daabcf&imgtype=0&src=http%3A%2F%2Fn.sinaimg.cn%2Ffront%2F589%2Fw750h639%2F20181126%2FdsnY-hpevhck7952010.jpg'
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
html=requests.get(url,headers=headers).content
with open('赵丽颖.jpg','wb') as f:
    f.write(html)
