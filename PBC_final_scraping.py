from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

option = webdriver.ChromeOptions()
option.add_argument('headless')

#啟動Chrome瀏覽器，連結到課程網頁面
driver = webdriver.Chrome('/Users/chenliangying/sublime/chromedriver', chrome_options=option)
url = 'https://nol2.aca.ntu.edu.tw/nol/guest/index.php'
driver.get(url)
driver.implicitly_wait(30)
start = time.time()
#進入登入畫面
driver.switch_to.frame(driver.find_element_by_xpath("/html/frameset/frameset/frame[1]"))
driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td/input").click()
#輸入帳號密碼（請自行輸入）
driver.find_element_by_name('user').clear()
driver.find_element_by_name('user').send_keys('')
driver.find_element_by_name('pass').clear()
driver.find_element_by_name('pass').send_keys('')
driver.find_element_by_name('Submit').click()

time.sleep(1)
# wait = WebDriverWait(driver, 10)
driver.switch_to.frame(driver.find_element_by_name('main'))  # 進入各式課程選欄
# element = wait.until(EC.element_to_be_clickable(By.XPATH, '/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/map/area[1]'))
# element.click()
driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/map/area[1]').click()
# time.sleep(2)
driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td[1]/a').click()  # 進入課程篩選頁面


# time.sleep(1)

#搜尋1000組課程資料
driver.find_element_by_xpath('//*[@id="page_cnt"]').clear()
driver.find_element_by_xpath('//*[@id="page_cnt"]').send_keys('1000')
driver.find_element_by_name("Submit22").click()
wait = WebDriverWait(driver, 30)
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/table[4]/tbody/tr[2]/td[5]/a')))


from bs4 import BeautifulSoup
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def clean_time(str1):
    weekdays = ['一', '二', '三', '四', '五', '六']
    time_clean = {}
    save = str()
    save_value = str()
    count = 0
    for i in str1:
        if i in weekdays:
            if save != '':
                time_clean[save] = [j for j in save_value.split(',')]
                save = i
                save_value = str()
            else:
                time_clean[i] = []
                save = i
        elif save != '':
            save_value += i
    if save_value != '':
        time_clean[save] = [j for j in save_value.split(',')]
    return time_clean

def clear_word_in_bracket(str1):
    while '(' in str1:
        list1 = [i for i in str1]
        for i in range(len(list1)):
            if list1[i] == '(':
                save = i
            elif list1[i] == ')':
                for j in range(i - save + 1):
                    list1.pop(save)
                break
        str1 = ''.join(list1)
        continue
    return str1


data = {}
odd = 0
same = 0
count = 0
odd_same = [[1, 0, 0]]
soup = BeautifulSoup(driver.page_source, 'html.parser')
c = soup.find_all('tr', {'align':'center'})
for i in c[1:]:
    if str(i.find_all('td')[0].text).isnumeric():
        if i.find_all('td')[0].text in data.keys():
            same += 1
            odd_same[0][2] += 1
        else:
            data[i.find_all('td')[0].text] = []
            for j in i.find_all('td'):
                data[i.find_all('td')[0].text].append(j.text)
#                 if data[i.find_all('td')[0].text][12] == '\xa0':
#                     pass
#                 else:
#                     data[i.find_all('td')[0].text][12] = clean_time(re.sub('\(.*?\)','', data[i.find_all('td')[0].text][12].strip()))
            data[i.find_all('td')[0].text][12] = clean_time(clear_word_in_bracket(data[i.find_all('td')[0].text][12].strip()))
    else:
        odd += 1
        odd_same[0][1] += 1
print(odd_same[0])


for w in range(2, 15):
    odd_same.append([w, 0, 0])
    driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td[2]/select/option[' + str(w) + ']').click()
    time.sleep(25)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    c = soup.find_all('tr', {'align':'center'})
    for i in c[1:]:
        if str(i.find_all('td')[0].text).isnumeric():
            if i.find_all('td')[0].text in data.keys():
                same += 1
                odd_same[-1][2] += 1
            else:
    #             count +=1
    #             print(count)
                data[i.find_all('td')[0].text] = []
                for j in i.find_all('td'):
                    data[i.find_all('td')[0].text].append(j.text)
#                 if data[i.find_all('td')[0].text][12] == '\xa0':
#                     pass
#                 else:
#                     data[i.find_all('td')[0].text][12] = clean_time(re.sub('\(.*?\)','', data[i.find_all('td')[0].text][12].strip()))
                data[i.find_all('td')[0].text][12] = clean_time(clear_word_in_bracket(data[i.find_all('td')[0].text][12].strip()))
        else:
            odd += 1
            odd_same[-1][1] += 1
    print(odd_same[-1])


data_frame = pd.DataFrame(data)
file_path = '/Users/chenliangying/sublime/test.xlsx'
writer = pd.ExcelWriter(file_path)

#columns参数用于指定生成的excel中列的顺序    columns=['char','num']
data_frame.T.to_excel(writer, index=False,encoding='utf-8',sheet_name='Sheet')
writer.save()
end = time.time()
print(end - start)
# print(data_frame.T)

