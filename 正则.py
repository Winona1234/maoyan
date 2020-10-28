# -*- coding=utf-8 -*-
# @Time:2020/10/11 9:16 上午
# Author :王文娜
# @File:正则.py
# @Software:PyCharm
import re

html = '''<div class="animal">
    <p class="name">
		<a title="Tiger"></a>
    </p>
    <p class="content">
		Two tigers two tigers run fast
    </p>
</div>

<div class="animal">
    <p class="name">
		<a title="Rabbit"></a>
    </p>

    <p class="content">
		Small white rabbit white and white
    </p>
</div>'''

pattern = re.compile(
    '<div class="animal">.*?title="(.*?)".*?'
    'class="content">(.*?)</p>',
    re.S
)
r_list = pattern.findall(html)
print(r_list)
for i in r_list:
    print('动物名称',i[0].strip())
    print('动物描述',i[1].strip())
    print('*'*50)