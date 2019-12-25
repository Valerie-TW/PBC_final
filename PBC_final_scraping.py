from selenium import webdriver
import time


option = webdriver.ChromeOptions()
option.add_argument('headless')

#啟動Chrome瀏覽器，連結到課程網頁面
driver = webdriver.Chrome('/Users/chenliangying/sublime/chromedriver', chrome_options=option)
url = 'https://nol2.aca.ntu.edu.tw/nol/guest/index.php'
driver.get(url)

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

driver.switch_to.frame(driver.find_element_by_name('main'))  # 進入各式課程選欄

driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/map/area[1]').click()
time.sleep(0.5)
driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td[1]/a').click()  # 進入課程篩選頁面


time.sleep(0.5)

#搜尋1000組課程資料
driver.find_element_by_xpath('//*[@id="page_cnt"]').clear()
driver.find_element_by_xpath('//*[@id="page_cnt"]').send_keys('1000')
driver.find_element_by_name("Submit22").click()
time.sleep(30)


from bs4 import BeautifulSoup


def clean_time(str1):  # 把課程時間換成set形式
    weekdays = ['一', '二', '三', '四', '五', '六']
    ABCD_num = ['A', 'B', 'C', 'D']
    time_clean = set()
    save = str()
    for i in str1:
        if i in weekdays:
            save = i
        elif save != '' and i != ',':
            if i in ABCD_num:
                time_clean.add(ABCD_num.index(i) + 11 + 15 * weekdays.index(save))
            elif i.isnumeric() or i in ABCD_num:
                time_clean.add(int(i) + 15 * weekdays.index(save))
    return time_clean

def time_to_dict(str1):  # 把課程時間換成字典形式
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

def clear_word_in_bracket(str1):  # 把課程時間含的括號去除
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

raw_data = []  # 課程（沒有去掉重複流水號)
data = {}  # 課程（有去掉重複流水號)
odd = 0  # 沒有流水號的課程數量
same = 0  # 重複流水號的課程數量
odd_same = [[1, 0, 0]]  # 總計第幾頁的odd&same
soup = BeautifulSoup(driver.page_source, 'html.parser')
c = soup.find_all('tr', {'align':'center'})
  # 爬第一頁
  # 把正常時間資料放到最後，第12項換成set資料
for i in c[1:]:
    if str(i.find_all('td')[0].text).isnumeric():
        if i.find_all('td')[0].text in data.keys():
            same += 1
            odd_same[0][2] += 1
            raw_data.append([])
            for j in i.find_all('td'):
                raw_data[-1].append(j.text)
        else:
            data[i.find_all('td')[0].text] = []
            raw_data.append([])
            for j in i.find_all('td'):
                data[i.find_all('td')[0].text].append(j.text)
                raw_data[-1].append(j.text)
            if data[i.find_all('td')[0].text][12] == '\xa0':
                data[i.find_all('td')[0].text].append(time_to_dict(clear_word_in_bracket(data[i.find_all('td')[0].text][12].strip())))
                data[i.find_all('td')[0].text][12] = set()
            else:
                data[i.find_all('td')[0].text].append(time_to_dict(clear_word_in_bracket(data[i.find_all('td')[0].text][12].strip())))
                data[i.find_all('td')[0].text][12] = clean_time(clear_word_in_bracket(data[i.find_all('td')[0].text][12].strip()))
            if raw_data[-1][12] == '\xa0':
                raw_data[-1].append(time_to_dict(clear_word_in_bracket(raw_data[-1])))
                raw_data[-1][12] = set()
            else:
                raw_data[-1].append(time_to_dict(clear_word_in_bracket(raw_data[-1])))
                raw_data[-1][12] = clean_time(clear_word_in_bracket(raw_data[-1]))
    else:
        odd += 1
        odd_same[0][1] += 1
print(odd_same[0])


  # 爬第2~14頁
  # 把正常時間資料放到最後，第12項換成set資料
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
                raw_data.append([])
                for j in i.find_all('td'):
                    raw_data[-1].append(j.text)
            else:
                data[i.find_all('td')[0].text] = []
                raw_data.append([])
                for j in i.find_all('td'):
                    data[i.find_all('td')[0].text].append(j.text)
                    raw_data[-1].append(j.text)
                if data[i.find_all('td')[0].text][12] == '\xa0':
                    data[i.find_all('td')[0].text].append(time_to_dict(clear_word_in_bracket(data[i.find_all('td')[0].text][12].strip())))
                    data[i.find_all('td')[0].text][12] = set()
                else:
                    data[i.find_all('td')[0].text].append(time_to_dict(clear_word_in_bracket(data[i.find_all('td')[0].text][12].strip())))
                    data[i.find_all('td')[0].text][12] = clean_time(clear_word_in_bracket(data[i.find_all('td')[0].text][12].strip()))
                if raw_data[-1][12] == '\xa0':
                    raw_data[-1].append(time_to_dict(clear_word_in_bracket(raw_data[-1])))
                    raw_data[-1][12] = set()
                else:
                    raw_data[-1].append(time_to_dict(clear_word_in_bracket(raw_data[-1])))
                    raw_data[-1][12] = clean_time(clear_word_in_bracket(raw_data[-1]))
        else:
            odd += 1
            odd_same[-1][1] += 1
    print(odd_same[-1])

  # 把資料轉成dataframe
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
data_frame = pd.DataFrame(data)

  # 把dataframe放上google sheet
import pygsheets as pygsheets
client = pygsheets.authorize(service_account_file = '/Users/chenliangying/sublime/PBC2019-163fbb5f74ee.json')
sheet = client.open("PBC2019")
worksheet = sheet.worksheet_by_title('PBC_final')
worksheet.set_dataframe(data_frame.T, (1,1))


data_frame2 = pd.DataFrame(raw_data)
worksheet2 = sheet.worksheet_by_title('PBC_final_rawdata')
worksheet2.set_dataframe(data_frame2, (1,1))

  # 把資料轉成excel
file_path = '/Users/chenliangying/sublime/test.xlsx'
writer = pd.ExcelWriter(file_path)
#columns参数用于指定生成的excel中列的顺序    columns=['char','num']
data_frame.T.to_excel(writer, index=False, encoding='utf-8',sheet_name='Sheet')
writer.save()

end = time.time()
print(end - start)  # 計算程式執行時間


