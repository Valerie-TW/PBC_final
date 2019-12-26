# -*- coding: utf-8 -*-
"""
================================
@author Andy Y. Hsiao
@since December 11th, 2019
================================
"""
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import re

class Select(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.csv = pd.read_csv('PBC_final_rawdata.csv')
        self.a = pd.DataFrame(self.csv)
        self.course_list = self.a.values.tolist()
        self.create_widget()
    def create_widget(self):
        self.filter2 = []
        for i in self.a['2']:
            d2 = bool(i[0:2] == 'PE')
            self.filter2.append(d2)
        self.filter3 = []
        for i in self.a['4']:
            if len(i) < 5:
                self.filter3.append(False)
            else:
                d3 = bool(i[1:5] == '大學國文')
                self.filter3.append(d3)

        self.filter4 = []
        self.tag = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8']
        for i in self.a['15']:
            for j in self.tag:
                if j in str(i):
                    self.filter4.append(True)
                    break
                elif j == 'A8' and j not in str(i):
                    self.filter4.append(False)

        self.filter5 = []
        for i in self.a['4']:
            if len(i) < 11:
                self.filter5.append(False)
            else:
                d5 = bool(i[1:11] == '全民國防教育軍事訓練')
                self.filter5.append(d5)

        self.filter6 = []
        for _ in self.a['15']:
            self.match1 = re.search(r'英語授課', str(_))
            self.match2 = re.search(r'英文授課', str(_))
            if self.match1:
                d6 = bool(self.match1)
                self.filter6.append(d6)
            elif self.match2:
                d7 = bool(self.match2)
                self.filter6.append(d7)
            else:
                self.filter6.append(False)

        self.filter7 = []
        for i in range(len(self.filter2)):
            if self.filter2[i] == self.filter3[i] == self.filter4[i] == self.filter5[i] == self.filter6[i] == False:
                self.filter7.append(True)
            else:
                self.filter7.append(False)


        self.labelTop1 = tk.Label(self, text="體育")
        self.labelTop1.grid(column=0, row=0)
        self.comboExample1 = ttk.Combobox(self, value=self.a[self.filter2].values.tolist(), width=50)
        # print(dict(comboExample1))
        self.comboExample1.grid(column=0, row=1)
        self.comboExample1.current(0)

        self.btn1 = tk.Button(self, text="add", width=15,
                         height=2, command=self.add1)
        self.btn1.grid(column=1, row=1)

        self.btn11 = tk.Button(self, text="remove", width=15,
                         height=2, command=self.remove1)
        self.btn11.grid(column=2, row=1)

        self.labelTop2 = tk.Label(self, text="大學國文")
        self.labelTop2.grid(column=0, row=2)
        self.comboExample2 = ttk.Combobox(self, value=self.a[self.filter3].values.tolist(), width=50)
        # print(dict(comboExample2))
        self.comboExample2.grid(column=0, row=3)
        self.comboExample2.current(0)

        self.btn2 = tk.Button(self, text="add", width=15,
                         height=2, command=self.add2)
        self.btn2.grid(column=1, row=3)

        self.btn22 = tk.Button(self, text="remove", width=15,
                         height=2, command=self.remove2)
        self.btn22.grid(column=2, row=3)

        self.labelTop3 = tk.Label(self, text="通識")
        self.labelTop3.grid(column=0, row=4)
        self.comboExample3 = ttk.Combobox(self, value=self.a[self.filter4].values.tolist(), width=50)
        self.comboExample3.grid(column=0, row=5)
        self.comboExample3.current(0)

        self.btn3 = tk.Button(self, text="add", width=15,
                         height=2, command=self.add3)
        self.btn3.grid(column=1, row=5)

        self.btn33 = tk.Button(self, text="remove", width=15,
                         height=2, command=self.remove3)
        self.btn33.grid(column=2, row=5)

        self.labelTop4 = tk.Label(self, text="軍訓")
        self.labelTop4.grid(column=0, row=6)
        self.comboExample4 = ttk.Combobox(self, value=self.a[self.filter5].values.tolist(), width=50)
        self.comboExample4.grid(column=0, row=7)
        self.comboExample4.current(0)

        self.btn4 = tk.Button(self, text="add", width=15,
                         height=2, command=self.add4)
        self.btn4.grid(column=1, row=7)

        self.btn44 = tk.Button(self, text="remove", width=15,
                         height=2, command=self.remove4)
        self.btn44.grid(column=2, row=7)

        self.labelTop5 = tk.Label(self, text="英語授課")
        self.labelTop5.grid(column=0, row=8)
        self.comboExample5 = ttk.Combobox(self, value=self.a[self.filter6].values.tolist(), width=50)
        self.comboExample5.grid(column=0, row=9)
        self.comboExample5.current(0)

        self.btn5 = tk.Button(self, text="add", width=15,
                         height=2, command=self.add5)
        self.btn5.grid(column=1, row=9)

        self.btn55 = tk.Button(self, text="remove", width=15,
                         height=2, command=self.remove5)
        self.btn55.grid(column=2, row=9)

        self.labelTop6 = tk.Label(self, text="選修")
        self.labelTop6.grid(column=0, row=10)
        self.comboExample6 = ttk.Combobox(self, value=self.a[self.filter7].values.tolist(), width=50)
        self.comboExample6.grid(column=0, row=11)
        self.comboExample6.current(0)

        self.btn6 = tk.Button(self, text="add", width=15,
                         height=2, command=self.add6)
        self.btn6.grid(column=1, row=11)

        self.btn66 = tk.Button(self, text="remove", width=15,
                         height=2, command=self.remove6)
        self.btn66.grid(column=2, row=11)

        self.course = str()
        self.list = []

    def add1(self):
        global course
        self.course = self.comboExample1.get()
        self.addToCart()

    def add2(self):
        global course
        self.course = self.comboExample2.get()
        self.addToCart()

    def add3(self):
        global course
        self.course = self.comboExample3.get()
        self.addToCart()

    def add4(self):
        global course
        self.course = self.comboExample4.get()
        self.addToCart()

    def add4(self):
        global course
        self.course = self.comboExample4.get()
        self.addToCart()

    def add5(self):
        global course
        self.course = self.comboExample5.get()
        self.addToCart()

    def add6(self):
        global course
        self.course = self.comboExample6.get()
        self.addToCart()

    def remove1(self):
        global course
        self.course = self.comboExample1.get()
        self.removeFromCart()

    def remove2(self):
        global course
        self.course = self.comboExample2.get()
        self.removeFromCart()

    def remove3(self):
        global course
        self.course = self.comboExample3.get()
        self.removeFromCart()

    def remove4(self):
        global course
        self.course = self.comboExample4.get()
        self.removeFromCart()

    def remove5(self):
        global course
        self.course = self.comboExample5.get()
        self.removeFromCart()

    def remove6(self):
        global course
        self.course = self.comboExample6.get()
        self.removeFromCart()

    def addToCart(self):
        if self.course in self.list:
            tk.messagebox.showerror(title='Error', message=self.course+" was added before!")
        elif self.course == "--Select a flavor--":
            tk.messagebox.showerror(title='Error', message="Please select a flavor!")
        else:
            self.list.append(self.course)
            tk.messagebox.showerror(title='Success', message=self.course+" has been added!")
            print(self.list)

    def removeFromCart(self):
        if self.course in self.list:
            self.list.remove(self.course)
            tk.messagebox.showerror(title='Success', message=self.course+" has been removed!")
            print(self.list)
        elif self.course == "--Select a flavor--":
            tk.messagebox.showerror(title='Error', message="Please select a flavor!")
        else:
            tk.messagebox.showerror(title='Error', message=self.course+" wasn't added!")

s = Select()
s.master.grid_rowconfigure(0, weight=1)
s.master.grid_columnconfigure(0, weight=1)
w, h = s.master.maxsize()
s.master.geometry("{}x{}".format(w, h))
s.master.title('課表')
s.mainloop()
