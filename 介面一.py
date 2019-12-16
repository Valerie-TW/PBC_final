import tkinter as tk
import tkinter.font as tkFont

class Window(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.create_widget()
    def create_widget(self):
        self.txt = tk.Text(height=1, width=10)
        tkFont.Font(size=32, family="Courier New")
        which_date = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
        date = dict()
        for i in range(7):
            date[i] = which_date[i]
        time = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'B', 'C', 'D']
        period = dict()
        for i in range(15):
            period[i] = time[i]
        self.lb1 = {}
        for i in range(7):
            self.lb1[i] = tk.Label(self, text=date[i], bg="green", fg="white")
            self.lb1[i].grid(row=0, column=i + 1)
            '''self.lb[i].pack(side='left')'''
        self.lb2 = {}
        for i in range(15):
            self.lb2[i] = tk.Label(self, text=period[i], bg="green", fg="white")
            self.lb2[i].grid(row=i + 1, column=0)
        self.btn = {}
        for i in range(105):
            self.btn[i] = tk.Button(self, width=8, height=2, bg="gray", command=lambda f=i: self.change_color(f))
            self.btn[i].grid(row=int(i / 7) + 1, column=i % 7 + 1, sticky=tk.SE + tk.NW)

    def change_color(self, index):
        self.btn[index].configure(bg='green')







calendar = Window()
calendar.master.title('課表')
calendar.mainloop()