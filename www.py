# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 13:45:59 2021

@author: linn2
"""
soup = BeautifulSoup(data.text,'html.parser')

divs = soup.find_all('div', class_='type02_bd-a')

for each_div in divs:

    h4 = each_div.find('h4')
    a = h4.find('a')
    bookname = a.text
    print(bookname)