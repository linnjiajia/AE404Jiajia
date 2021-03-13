# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 14:04:35 2020

@author: linn2
"""

import tkinter as tk

window = tk.Tk()

window.title("我的第一個GUT程式")

window.geometry('300x300')

label = tk.Label(window, text="Jiajia")
label.pack()

entry = tk.Entry(window, width=30)
entry.pack()

button = tk.Button(window, text="click me!")
button.pack()

window.mainloop()







