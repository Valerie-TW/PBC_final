# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import re

class basedesk():
    def __init__(self,master):
        self.root = master    
        Window(self.root)      
class Window(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self)
        self.master = master
        self.configure(bg='#FFFFE0')
        self.grid()
        self.create_widget()
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        w, h = self.master.maxsize()
        self.master.geometry("{}x{}".format(w, h))
        self.master.title('課表')
    def create_widget(self):
        self.fbtn = tk.Button(self, text='確定送出', width=15, height=1, bg="white", fg="black",font='微軟正黑體 8', command=self.change)
        self.fbtn.grid(row=0, column=9)
        self.flb = tk.Label(self, text='選擇系所', bg='#8B795E', fg='white',font='微軟正黑體 12')
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
        time = ['0\n7:10~8:00', '1\n8:10~9:00','2\n9:10~10:00', '3\n10:20~11:10', '4\n11:20~12:10', '5\n12:20~13:10', '6\n13:20~14:10', '7\n14:20~15:10', '8\n15:30~16:20', '9\n16:30~17:20', '10\n17:30~18:20', 'A\n18:25~19:15', 'B\n19:20~20:10', 'C\n20:15~21:05', 'D\n21:10~22:00']
        period = dict()
        for i in range(15):
            period[i] = time[i]
        self.lb1 = dict()
        for i in range(7):
            self.lb1[i] = tk.Label(self, text=date[i], bg="#8B795E", fg="white",font='微軟正黑體 12')
            self.lb1[i].grid(row=0, column=i + 1)
            '''self.lb[i].pack(side='left')'''
        self.lb2 = dict()
        for i in range(15):
            self.lb2[i] = tk.Label(self, text=period[i], bg="#8B795E", fg="white",font='微軟正黑體 8',width ='8',height='2')
            self.lb2[i].grid(row=i + 1, column=0)
        self.btn = dict()
        for i in range(105):
            '''self.btn[i] = tk.Button(self, width=8, height=2, bg="gray", command=lambda f=i: self.change_color(f))'''
            self.btn[i] = tk.Button(self, width=8, height=2, bg="#8B8B83", command=lambda f=i: self.click(f))
            self.btn[i].grid(row=i % 15 + 1, column=int(i / 15) + 1, sticky=tk.N + tk.E + tk.S + tk.W)

    '''def change_color(self, index):
        self.btn[index].configure(bg='green')'''
    add = dict()
    for j in range(105):
        add[j] = 0
    information = []

    def click(self, index):
        if self.add[index] % 2 != 0:  # 取消選課
            self.btn[index].configure(bg='#8B8B83')
            self.add[index] += 1
            self.information.remove(index)
        else:  # 選課
            self.btn[index].configure(bg='#C1FFC1')
            self.add[index] += 1
            self.information.append(index)

    def send(self):
        global my_course
        my_course = []
        for i in self.information:
            my_course.append(i)

    def change(self):
        global my_course
        my_course = []
        for i in self.information:
            my_course.append(i)
        self.destroy()
        Select(tk.Frame)


    '''print(self.information)'''

    '''self.information[self.lb1[int(index / 7)]] = self.lb2[int(index / 7)]'''

class Select(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self)
        self.master = master
        self.configure(bg='#FFFFE0')
        self.grid()

        googleSheetId = '1AofDa53X_w1VbCXRpz_Ete6BXuQTdnVAjsWCFip9weM'
        worksheetName = 'PBC_final_rawdata'
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(googleSheetId,worksheetName)
        self.csv = pd.read_csv(url)
        self.a = pd.DataFrame(self.csv)

        # self.csv = pd.read_csv('PBC_final.csv')
        # self.a = pd.DataFrame(self.csv)
        self.course_list = self.a.values.tolist()
        self.create_widget()
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        w, h = self.master.maxsize()
        self.master.geometry("{}x{}".format(w, h))
        self.master.title('課表')
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


if __name__ == '__main__':
    root = tk.Tk()
    root.configure(bg='#FFFFE0')
    basedesk(root)
    root.mainloop()
