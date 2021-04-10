# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 14:10:39 2021

@author: linn2
"""
import re
number = input('輸入gmail帳號')
if re.fullmatch("\w+@gmail.com$",number) != None:
    print('以儲存你的gmail帳號')
else:
    print('gmail帳號格式錯誤')