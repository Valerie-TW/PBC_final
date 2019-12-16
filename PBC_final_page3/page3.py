import tkinter as tk
from tkinter import ttk 


class window(tk.Frame) :
    def __init__(self, selected_course) :
        tk.Frame.__init__(self)
        self.course = selected_course
        self.pack()     
        self.deliver_btn()
        self.text_title()
        self.print_course()
    def text_title(self) :
        self.title = tk.Label(text='已選課程',fg='#8B814C',bg='#FFFFE0',font='微軟正黑體 15')
        self.title.pack()
    def deliver_btn(self) :
        self.btn = tk.Button(text='送出表單',bg= '#CDBA96')
        self.img = tk.PhotoImage(file=r"C:\Users\jk520\OneDrive\桌面\PBC_final\PBC_final_page3\3.png")
        self.btn.config(image=self.img)
        self.btn.pack(side='bottom')

    def print_course(self) :
        flag = True
        for key,value in self.course.items():    
            self.lab = tk.Label(text=value,font='微軟正黑體 10',width ='100',height='2',bg=('#FFFACD' if flag else '#EEE8CD'))
            self.lab.pack()
            flag = not flag



course = {'01001':'CHIN1081 01 大學國文一','44747':'圖資系	LIS1004	參考資源','30904':'圖資系 LIS1003 01 服務學習三'}
root = window(course) 
root.master.title('已選課程')
root.master.configure(bg='#FFFFE0')
root.master.resizable(1,1)
root.master.geometry('400x200')
root.mainloop()





