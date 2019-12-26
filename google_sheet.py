import pandas as pd
googleSheetId = '1AofDa53X_w1VbCXRpz_Ete6BXuQTdnVAjsWCFip9weM'
worksheetName = 'PBC_final_rawdata'
pd.set_option('display.max_columns', None)  # 讓dataframe完整呈現，不因量多簡化呈現
pd.set_option('display.max_rows', None)  # 讓dataframe完整呈現，不因量多簡化呈現
url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
    googleSheetId,
    worksheetName
)
csv = pd.read_csv(url)
a = pd.DataFrame(csv)
my_course = {1,3,5,7,9,13,14,16,22,24,25,33,38,41,46}
filter1 = []
for i in a['12']:
    if i[1:-1] == '':
        filter1.append(set(i[1:-1]) & my_course == set())
    else:
        list1 = [int(j) for j in i[1:-1].split(',')]
        filter1.append(set(list1) & my_course == set())

print(a[filter1])