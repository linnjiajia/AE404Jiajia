# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 14:43:25 2021

@author: linn2
"""

import json
import requests

url = 'https://www.dcard.tw/service/api/v2/forums/pet/posts?limit=1&before=235778028'
respond = requests.get(url)

jsonData = json.loads(respond.text)
D = {}
for data in jsonData:
    D['title']=data['title']
    
    
    
    with open('Dcard.json', 'a', encoding='utf-8') as f:
       json.dump(D, f, ensure_ascii=False) 