# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

class Window(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.create_widget()
    def create_widget(self):
        self.fbtn = tk.Button(self, text='確定送出', width=15, height=1, bg="white", fg="black")
        self.fbtn.grid(row=0, column=9)
        self.flb = tk.Label(self, text='選擇系所', bg='white', fg='black')
        self.flb.grid(row=1, column=9)
        with open(file='系所.txt', mode='r', encoding='utf-8') as f:
            all_coll = f.readlines()
        self.college= ttk.Combobox(self, values=all_coll)
        self.college.grid(row=2, column=9)
        self.college.current(0)
        '''self.txt = tk.Text(height=1, width=10)'''
        tkFont.Font(size=32, family="Courier New")
        which_date = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
        date = dict()
        for i in range(7):
            date[i] = which_date[i]
        time = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'B', 'C', 'D']
        period = dict()
        for i in range(15):
            period[i] = time[i]
        self.lb1 = dict()
        for i in range(7):
            self.lb1[i] = tk.Label(self, text=date[i], bg="green", fg="white")
            self.lb1[i].grid(row=0, column=i + 1)
            '''self.lb[i].pack(side='left')'''
        self.lb2 = dict()
        for i in range(15):
            self.lb2[i] = tk.Label(self, text=period[i], bg="green", fg="white")
            self.lb2[i].grid(row=i + 1, column=0)
        self.btn = dict()
        for i in range(105):
            '''self.btn[i] = tk.Button(self, width=8, height=2, bg="gray", command=lambda f=i: self.change_color(f))'''
            self.btn[i] = tk.Button(self, width=8, height=2, bg="gray", command=lambda f=i: self.click(f))
            self.btn[i].grid(row=i % 15 + 1, column=int(i / 15) + 1, sticky=tk.N + tk.E + tk.S + tk.W)

    '''def change_color(self, index):
        self.btn[index].configure(bg='green')'''
    add = dict()
    for j in range(105):
        add[j] = 0
    information = []

    def click(self, index):
        if self.add[index] % 2 != 0:  # 取消選課
            self.btn[index].configure(bg='gray')
            self.add[index] += 1
            self.information.remove(index)
        else:  # 選課
            self.btn[index].configure(bg='green')
            self.add[index] += 1
            self.information.append(index)
        print(self.information)

        '''self.information[self.lb1[int(index / 7)]] = self.lb2[int(index / 7)]'''


calendar = Window()
'''calendar.master.resizable(0, 0)'''
'''calendar.master.geometry("400x200")'''
calendar.master.grid_rowconfigure(0, weight=1)
calendar.master.grid_columnconfigure(0, weight=1)
w, h = calendar.master.maxsize()
calendar.master.geometry("{}x{}".format(w, h))
calendar.master.title('課表')
calendar.mainloop()