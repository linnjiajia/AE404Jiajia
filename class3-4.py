# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 14:30:50 2021

@author: linn2
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.books.com.tw/web/sys_saletopb/books/'
data = requests.get(url)

soup = BeautifulSoup(data.text,'html.parser')

divs = soup.find_all('img', class_='cover')

for each_div in divs[:3]:
    img = each_div['src']
    alt = each_div['alt']

    imgRespond = requests.get(img)
    with open(alt+'.jpg', 'wb') as f:
        f.write(imgRespond.content)
    