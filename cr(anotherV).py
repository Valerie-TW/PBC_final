import pandas as pd

def get_selected_course(target_index):
    googleSheetId = '1AofDa53X_w1VbCXRpz_Ete6BXuQTdnVAjsWCFip9weM'
    worksheetName = 'PBC_final_rawdata'
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
        googleSheetId,
        worksheetName
    )
    csv = pd.read_csv(url)
    a = pd.DataFrame(csv)
    print(target_index)
    list1 = []
    course = a[a['0'].isin(target)][['0','1', '4', '6' , '7', '9', '10', '11', '14', '15']]
    for j in range(len(course)):
        list1.append(' '.join(str(i) for i in course.iloc[j]).replace('\xa0', ''))
    return list1

target = [97001,97005,97022]
