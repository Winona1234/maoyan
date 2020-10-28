# -*- coding=utf-8 -*-
# @Time:2020/10/12 3:18 下午
# Author :王文娜
# @File:测试正则表达式.py
# @Software:PyCharm
import requests
import re
from useragents import ua_list
import random
headers={'user-agent':random.choice(ua_list)}

url='https://www.dytt8.net/html/gndy/dyzz/list_23_1.html'
res=requests.get(url,headers=headers,timeout=10).text
p_biao= '<table width="100%".*?<td height="26">.*?<a href="(.*?)".*?>(.*?)</a>'
biao=re.findall(p_biao,res,re.S)
print(biao)
<a href="#" target="_self" thunderpid="" thundertype="" thunderrestitle="ftp://ygdy8:ygdy8@yg69.dydytt.net:8021/阳光电影www.ygdy8.com.维塔利娜·瓦雷拉.BD.1080p.中英双字幕.mkv" onclick="return OnDownloadClick_Simple(this,2);" oncontextmenu="ThunderNetwork_SetHref(this)" thunderhref="thunder://QUFmdHA6Ly95Z2R5ODp5Z2R5OEB5ZzY5LmR5ZHl0dC5uZXQ6ODAyMS8lRTklOTglQjMlRTUlODUlODklRTclOTQlQjUlRTUlQkQlQjF3d3cueWdkeTguY29tLiVFNyVCQiVCNCVFNSVBMSU5NCVFNSU4OCVBOSVFNSVBOCU5QyVDMiVCNyVFNyU5MyVBNiVFOSU5QiVCNyVFNiU4QiU4OS5CRC4xMDgwcC4lRTQlQjglQUQlRTglOEIlQjElRTUlOEYlOEMlRTUlQUQlOTclRTUlQjklOTUubWt2Wlo=">ftp://ygdy8:ygdy8@yg69.dydytt.net:8021/阳光电影www.ygdy8.com.维塔利娜·瓦雷拉.BD.1080p.中英双字幕.mkv</a>