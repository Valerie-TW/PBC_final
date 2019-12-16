from selenium import webdriver
import time
#啟動Chrome瀏覽器，連結到課程網頁面
driver = webdriver.Chrome('/Users/chenliangying/sublime/chromedriver')
url = 'https://nol2.aca.ntu.edu.tw/nol/guest/index.php'
driver.get(url)
time.sleep(2)


#進入登入畫面
driver.switch_to.frame(driver.find_element_by_xpath("/html/frameset/frameset/frame[1]"))
driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td/input").click()
#輸入帳號密碼（請自行輸入）
driver.find_element_by_name('user').clear()
driver.find_element_by_name('user').send_keys('')
driver.find_element_by_name('pass').clear()
driver.find_element_by_name('pass').send_keys('')
driver.find_element_by_name('Submit').click()

time.sleep(2)
driver.switch_to.frame(driver.find_element_by_name('main'))  # 進入各式課程選欄
driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/map/area[1]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td[1]/a').click()  # 進入課程篩選頁面


time.sleep(1)

#搜尋1000組課程資料
driver.find_element_by_xpath('//*[@id="page_cnt"]').clear()
driver.find_element_by_xpath('//*[@id="page_cnt"]').send_keys('1000')
driver.find_element_by_name("Submit22").click()
time.sleep(30)


from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

print(soup.find_all('tr', {'align':'center'}))

#driver.switch_to.frame(driver.find_element_by_name('main'))
from bs4 import BeautifulSoup
import pandas as pd
soup = BeautifulSoup(driver.page_source, 'html.parser')
data = dict()
#print(soup.prettify())
c = soup.find_all('tr', {'align':'center'})
for i in c[1:]:
    #print(i.find_all('td'))
    data[i.find_all('td')[0].text] = []
    for j in i.find_all('td'):
        #print(j.text)
        data[i.find_all('td')[0].text].append(j.text)

    #print(data[i.find_all('td')[0]])

    #print('=========')
print(len(data.keys()))
for i in data.values():
    print(i[4], i[12].split('(')[0])


data_frame = pd.DataFrame(data)
data_frame.T
