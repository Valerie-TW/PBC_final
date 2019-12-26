# -*- coding: utf-8 -*-
"""
================================
@author Andy Y. Hsiao
@since December 11th, 2019
================================
"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import re

googleSheetId = '1AofDa53X_w1VbCXRpz_Ete6BXuQTdnVAjsWCFip9weM'
WorkSheetName = 'PBC_final'
url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(googleSheetId, WorkSheetName)
a = pd.read_csv(url)

course_list = a.values.tolist()


list100 =[1]

filter2 = []
for i in a['2']:
    d2 = bool(i[0:2] == 'PE')
    filter2.append(d2)

filter3 = []
for i in a['4']:
    if len(i) < 5:
        filter3.append(False)
    else:
        d3 = bool(i[1:5] == '大學國文')
        filter3.append(d3)

filter4 = []
tag = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8']
for i in a['15']:
    for j in tag:
        if j in str(i):
            filter4.append(True)
            break
        elif j == 'A8' and j not in str(i):
            filter4.append(False)

filter5 = []
for i in a['4']:
    if len(i) < 11:
        filter5.append(False)
    else:
        d5 = bool(i[1:11] == '全民國防教育軍事訓練')
        filter5.append(d5)

filter6 = []
for _ in a['15']:
    match1 = re.search(r'英語授課', str(_))
    match2 = re.search(r'英文授課', str(_))
    if match1:
        d6 = bool(match1)
        filter6.append(d6)
    elif match2:
        d7 = bool(match2)
        filter6.append(d7)
    else:
        filter6.append(False)

# 建立主視窗和 Frame（把元件變成群組的容器）
window = tk.Tk()
window.title("My Course")

# 設定視窗參數
window.geometry("1920x1080")  # 預設開啟大小
window.config(bg="lightyellow")  # 顏色
window.attributes("-alpha", 1)  # 透明度
# window.attributes("-topmost", 1)  # 置頂

course = str()

def add1():
    global course
    course = comboExample1.get()
    addToCart()

def add2():
    global course
    course = comboExample2.get()
    addToCart()

def add3():
    global course
    course = comboExample3.get()
    addToCart()

def add4():
    global course
    course = comboExample4.get()
    addToCart()

def add5():
    global course
    course = comboExample5.get()
    addToCart()

def add6():
    global course
    course = comboExample6.get()
    addToCart()

def remove1():
    global course
    course = comboExample1.get()
    removeFromCart()

def remove2():
    global course
    course = comboExample2.get()
    removeFromCart()

def remove3():
    global course
    course = comboExample3.get()
    removeFromCart()

def remove4():
    global course
    course = comboExample4.get()
    removeFromCart()

def remove5():
    global course
    course = comboExample5.get()
    removeFromCart()


def remove6():
    global course
    course = comboExample6.get()
    removeFromCart()


labelTop1 = tk.Label(window, text="體育")
labelTop1.grid(column=0, row=0)
comboExample1 = ttk.Combobox(window, value=a[filter2].values.tolist(), width=50)
# print(dict(comboExample1))
comboExample1.grid(column=0, row=1)
comboExample1.current(0)

btn1 = tk.Button(window, text="add", width=15,
                 height=2, command=add1)
btn1.grid(column=1, row=1)

btn11 = tk.Button(window, text="remove", width=15,
                  height=2, command=remove1)
btn11.grid(column=2, row=1)

labelTop2 = tk.Label(window, text="大學國文")
labelTop2.grid(column=0, row=2)
comboExample2 = ttk.Combobox(window, value=a[filter3].values.tolist(), width=50)
# print(dict(comboExample2))
comboExample2.grid(column=0, row=3)
comboExample2.current(0)

btn2 = tk.Button(window, text="add", width=15,
                 height=2, command=add2)
btn2.grid(column=1, row=3)

btn22 = tk.Button(window, text="remove", width=15,
                  height=2, command=remove2)
btn22.grid(column=2, row=3)

labelTop3 = tk.Label(window, text="通識")
labelTop3.grid(column=0, row=4)
comboExample3 = ttk.Combobox(window, value=a[filter4].values.tolist(), width=50)
# print(dict(comboExample3))
comboExample3.grid(column=0, row=5)
comboExample3.current(0)

btn3 = tk.Button(window, text="add", width=15,
                 height=2, command=add3)
btn3.grid(column=1, row=5)

btn33 = tk.Button(window, text="remove", width=15,
                  height=2, command=remove3)
btn33.grid(column=2, row=5)

labelTop4 = tk.Label(window, text="軍訓")
labelTop4.grid(column=0, row=6)
comboExample4 = ttk.Combobox(window, value=a[filter5].values.tolist(), width=50)
# print(dict(comboExample4))
comboExample4.grid(column=0, row=7)
comboExample4.current(0)

btn4 = tk.Button(window, text="add", width=15,
                 height=2, command=add4)
btn4.grid(column=1, row=7)

btn44 = tk.Button(window, text="remove", width=15,
                  height=2, command=remove4)
btn44.grid(column=2, row=7)

labelTop5 = tk.Label(window, text="英語授課")
labelTop5.grid(column=0, row=8)
comboExample5 = ttk.Combobox(window, value=a[filter6].values.tolist(), width=50)
# print(dict(comboExample5))
comboExample5.grid(column=0, row=9)
comboExample5.current(0)

btn5 = tk.Button(window, text="add", width=15,
                 height=2, command=add5)
btn5.grid(column=1, row=9)

btn55 = tk.Button(window, text="remove", width=15,
                  height=2, command=remove5)
btn55.grid(column=2, row=9)

labelTop6 = tk.Label(window, text="Fresh Milk Tea")
labelTop6.grid(column=0, row=10)
comboExample6 = ttk.Combobox(window, value=list100, width=50)
# print(dict(comboExample6))
comboExample6.grid(column=0, row=11)
comboExample6.current(0)

btn6 = tk.Button(window, text="add", width=15,
                 height=2, command=add6)
btn6.grid(column=1, row=11)

btn66 = tk.Button(window, text="remove", width=15,
                  height=2, command=remove6)
btn66.grid(column=2, row=11)

list = []


def addToCart():
    if course in list:
        tk.messagebox.showerror(title='Error', message=course+" was added before!")
    elif course == "--Select a flavor--":
        tk.messagebox.showerror(title='Error', message="Please select a flavor!")
    else:
        list.append(course)
        tk.messagebox.showerror(title='Success', message=course+" has been added!")
        print(list)


def removeFromCart():
    if course in list:
        list.remove(course)
        tk.messagebox.showerror(title='Success', message=course+" has been removed!")
        print(list)
    elif course == "--Select a flavor--":
        tk.messagebox.showerror(title='Error', message="Please select a flavor!")
    else:
        tk.messagebox.showerror(title='Error', message=course+" wasn't added!")
window.mainloop()
