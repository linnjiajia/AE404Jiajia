# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 14:01:02 2021

@author: linn2
"""

import json

data = {
        'Name': "Eric",
        'height': 180.5,
        "Male": True,
        }
jsonData = json.dumps(data)

with open('practice.json', 'w') as f:
    f.write(jsonData)
    
with open('practice.json', 'r') as f:
    text = json.load(f)
    
print(text['height'])