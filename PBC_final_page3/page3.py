import tkinter as tk
from tkinter import ttk 
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

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
        self.btn = tk.Button(text='送出表單',bg= '#CDBA96',command=self.import_course)
        self.img = tk.PhotoImage(file=r"./3.png")
        self.btn.config(image=self.img)
        self.btn.pack(side='bottom')
    def print_course(self) :
        flag = True
        for key,value in self.course.items():    
            self.lab = tk.Label(text=value,font='微軟正黑體 10',width ='100',height='2',bg=('#FFFACD' if flag else '#EEE8CD'))
            self.lab.pack()
            flag = not flag

    def import_course(self) :
        driver = webdriver.Chrome(r'..\chromedriver.exe')
        url = 'https://nol2.aca.ntu.edu.tw/nol/guest/index.php'
        driver.get(url)
        time.sleep(2)

        #進入登入畫面
        driver.switch_to.frame(driver.find_element_by_xpath("/html/frameset/frameset/frame[1]"))
        driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td/input").click()
        #輸入帳號密碼（請自行輸入）
        driver.find_element_by_name('user').clear()
        driver.find_element_by_name('user').send_keys(account.get())
        driver.find_element_by_name('pass').clear()
        driver.find_element_by_name('pass').send_keys(password.get())
        driver.find_element_by_name('Submit').click()

        time.sleep(1)
        driver.switch_to.frame(driver.find_element_by_name('main'))  # 進入各式課程選欄
        driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/map/area[1]').click()
        driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td[1]/a').click()  # 進入課程篩選頁面

        select_button = Select(driver.find_element_by_id('cstype')) 
        select_button.select_by_visible_text('流水號')

        number_list = ['01001','44747']
        for number in number_list :
            driver.find_element_by_id('csname').clear()
            driver.find_element_by_id('csname').send_keys(number)
            driver.find_element_by_name("Submit22").click()
            # driver.switch_to.frame(driver.find_element_by_name('main'))
            driver.find_element_by_xpath("/html/body/table[4]/tbody/tr[2]/td[18]").click()

number_list = ['01001','44747']
course = {'01001':'CHIN1081 01 大學國文一','44747':'圖資系	LIS1004	參考資源','30904':'圖資系 LIS1003 01 服務學習三'}
root = window(course) 
root.master.title('已選課程')
root.master.configure(bg='#FFFFE0')
root.master.resizable(1,1)
# root.master.geometry('')
# w, h = root.master.maxsize()
# root.master.geometry("{}x{}".format(w, h))
# //////
account = tk.StringVar()
password = tk.StringVar()
lab_account = tk.Label(text='帳號',font='微軟正黑體 10',fg='#8B814C',bg='#FFFFE0')
entry_account = tk.Entry(textvariable=account)
lab_password = tk.Label(text='密碼',font='微軟正黑體 10',fg='#8B814C',bg='#FFFFE0')
entry_password = tk.Entry(textvariable=password,show='*')
lab_account.pack()
entry_account.pack()
lab_password.pack()
entry_password.pack()
root.mainloop()

