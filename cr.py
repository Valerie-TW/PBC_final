import sys
import time
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
import pygsheets
def get_selected_course(target_index):
    """
    target_index = []
    """
    googleSheetId = '1AofDa53X_w1VbCXRpz_Ete6BXuQTdnVAjsWCFip9weM'
    WorkSheetName = 'PBC_final'
    D = ['1','3','5','12', '16','17']
    # gc = pygsheets.authorize(service_file=r'..\PBC2019-163fbb5f74ee.json')
    url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(googleSheetId,WorkSheetName)
    frame = pd.read_csv(url)
    frame = frame.drop(columns=D)
    # print(type(frame))
    # print(frame.row)
    # sh = url.open('PBC2019')
    # wks = sh[2]

    # frame = wks.get_as_df().drop(D,1)
    result = frame['0'].isin(target_index)
    # print(frame[result])
    return frame[result].values
    # return frame
target = [97001,97005,97022]
# print(get_selected_course(target))