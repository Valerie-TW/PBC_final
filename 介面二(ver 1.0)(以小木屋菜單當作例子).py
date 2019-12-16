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


S_W_waffles = ['--Select a flavor--', 'Original', 'Honey', 'Caramelized Sugar',
               'Condensed Milk', 'Whipped Cream', 'Blueberry Jelly', 'Peanut Paste',
               'Matcha Paste', 'Coconut Paste', 'Chocolate Spread', 'Honey & Whipped Cream',
               'Caramelized Sugar & Whipped Cream', 'Vanilla Custard',
               'Chocolate Spread & Whipped Cream', 'Coconut Paste with Raisin',
               'Condensed Milk & Red Bean Paste', 'Black Sesame & Peanut Paste',
               'Blueberry Jelly with Sliced Cheese', 'Chocolate Spread & Peanut Paste',
               'Chocolate Spread & Banana', 'Red Bean & Whipped Cream', 'Matcha Paste & Red Bean',
               'Blueberry Jelly & Vanilla Custard', 'Chocolate Spread & Vanilla Custard']

S_F_waffles = ['--Select a flavor--', 'Corn with Vegetables', 'Cheese with Vegetables',
               'Smoked Chicken with Vegetables', 'Beef Burger with Vegetables',
               'Spicy Chicken with Vegetables', 'Tuna Salad with Vegetables',
               'New Orieans Roasted Chicken with Vegetables',
               'Sliced Pork in Terlyaki Sauce with Vegetables',
               'BBQ Chicken Thigh with Vegetables',
               'Chicken Thigh in Basil Sauce with Vegetables',
               'Bacon & Peanut Paste with Vegetables',
               'Korean Flavor Spicy Chicken Thigh with Vegetables',
               'Spicy Chicken & Bacon  with Vegetables',
               'Jalapeno Slices & Chicken  with Vegetables',
               'Jalapeno Slices & Beef Burger with Vegetables',
               'Beef Burger & Bacon, Peanut Paste with Vegetables',
               'BBQ Chicken Thigh & Bacon, Peanut Paste with Vegetables'
               ]

F_F_waffles = ['--Select a flavor--', 'Brown Pattles with Sliced Cheese',
               'Golden Pork Cutlet with Sliced Cheese',
               'Spicy Fried Chicken Thigh with Sliced Cheese',
               'Original Fried Chicken Thigh with Sliced Cheese',
               ]

Fried_snacks = ['--Select a flavor--','Brown Patties',
                'Golden Crispy Fries', 'Tender Chicken Nuggets',
                'Spicy Popcorn Chicken', 'Original Popcorn Chicken']

Tea = ['--Select a flavor--', 'Assam Black Tea', 'Premium Jin Xuan Tea',
       'Toffee Black Tea', 'Gyokuro Green Tea', 'Earl Grey Tea',
       'Rose Black Tea', 'Lichee Black Tea', 'Orange Fruit Tea']

Fresh_Milk_Tea = ['--Select a flavor--', 'British-style Tea with Fresh Milk',
                  'White Gourd  with Fresh Milk', 'Tieguanyin  with Fresh Milk',
                  'Earl Grey Tea with Fresh Milk', 'Rose Black Tea with Fresh Milk',
                  'Lichee Black Tea with Fresh Milk',
                  'Matcha  with Fresh Milk', 'Chocolote  with Fresh Milk']

H_B_without_Caffeine = ['--Select a flavor--', 'White Gourd Water',
                        'White Gourd Lemon Juice', 'Honey Lemon Juice',
                        'Strawberry & Raspberry Fruit Tea',
                        'Cranberry Flavor Frozen Tea(Summer Limited)',
                        'Lichee Flavor Frozen Tea(Summer Limited)'
                        'Longan Juice Tea(Winter Limited)',
                        'Brown Sugar Ginger Tea(Winter Limited)']

Italian_coffee = ['--Select a flavor--', 'Coffee Americano', 'Latte',
                  'Cappuccino', 'Hazelnut Latte', 'Caramel Latte',
                  'Toffee Latte']

# 建立主視窗和 Frame（把元件變成群組的容器）
window = tk.Tk()
window.title("NTU Food")
window.top_frame = tk.Frame().pack()
window.bottom_frame = tk.Frame().pack()
"""
# 將元件分為 top/bottom 兩群並加入主視窗
window.top_frame.grid()
window.bottom_frame.grid(side=tk.BOTTOM)
"""
im = Image.open('waffle.jpg')
img = ImageTk.PhotoImage(im)


# 設定視窗參數
window.geometry("1920x1080")  # 預設開啟大小
"""
window.minsize(width=640, height=300)  # 縮放最小大小
window.maxsize(width=1920, height=1080)  # 縮放最大大小
"""
window.config(bg="lightyellow")  # 顏色
window.attributes("-alpha", 1)  # 透明度
window.attributes("-topmost", 1)  # 置頂

labelTop1 = tk.Label(window, text="Sweet Flavor Waffles")
labelTop1.pack()
comboExample1 = ttk.Combobox(window, value=S_W_waffles, width=50)
print(dict(comboExample1))
comboExample1.pack()
comboExample1.current(0)

labelTop2 = tk.Label(window, text="Salty Flavor Waffles")
labelTop2.pack()
comboExample2 = ttk.Combobox(window, value=S_F_waffles, width=50)
print(dict(comboExample2))
comboExample2.pack()
comboExample2.current(0)

labelTop3 = tk.Label(window, text="Fried Flavor Waffles")
labelTop3.pack()
comboExample3 = ttk.Combobox(window, value=F_F_waffles, width=50)
print(dict(comboExample3))
comboExample3.pack()
comboExample3.current(0)


labelTop4 = tk.Label(window, text="Fried Snacks")
labelTop4.pack()
comboExample4 = ttk.Combobox(window, value=Fried_snacks, width=50)
print(dict(comboExample4))
comboExample4.pack()
comboExample4.current(0)

labelTop5 = tk.Label(window, text="Tea")
labelTop5.pack()
comboExample5 = ttk.Combobox(window, value=Tea, width=50)
print(dict(comboExample5))
comboExample5.pack()
comboExample5.current(0)


labelTop6 = tk.Label(window, text="Fresh Milk Tea")
labelTop6.pack()
comboExample6 = ttk.Combobox(window, value=Fresh_Milk_Tea, width=50)
print(dict(comboExample6))
comboExample6.pack()
comboExample6.current(0)

labelTop7 = tk.Label(window, text="Healthy Beverage without Caffeine")
labelTop7.pack()
comboExample7 = ttk.Combobox(window, value=H_B_without_Caffeine, width=50)
print(dict(comboExample7))
comboExample7.pack()
comboExample7.current(0)


labelTop8 = tk.Label(window, text="Italian Coffee")
labelTop8.pack()
comboExample8 = ttk.Combobox(window, value=Italian_coffee, width=50)
print(dict(comboExample8))
comboExample8.pack()
comboExample8.current(0)

btn2 = tk.Button(window.bottom_frame, text='Order & Pay', width=30,
                 height=5)
btn2.pack(side='bottom')

btn1 = tk.Button(window.bottom_frame, text='Add to Cart', width=30,
                 height=5)
btn1.pack(side='bottom')

window.mainloop()



# 以下是menubar
"""
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)

submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='Import', menu=submenu, underline=0)
submenu.add_command(label="Submenu1", command=do_job)

window.config(menu=menubar)
"""
"""
btn2 = tk.Button(window,
                 text='Add to Cart',
                 )
btn2.pack()
"""
