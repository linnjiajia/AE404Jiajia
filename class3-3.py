# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 14:01:00 2021

@author: linn2
"""

f = open('blablabla.txt', 'w')
f.write('翁老真的很雞掰')
f.close()

f = open('blablabla.txt', 'a')
f.write('我撿到錢包是關他屁事')
f.close()

f = open('blablabla.txt', 'r')
text = f.read()
f.close()

print(text)