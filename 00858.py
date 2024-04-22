from configparser import ConfigParser
import pandas as pd

from Rainbow import connectlib, requestlib
from io import StringIO

import time
import os
import shutil

import win32com.client as win32

def STOXX_DATA(_RAW):
    _result = _RAW.replace(';', ',')
    _result = StringIO(_result[:])
    result = pd.read_csv(_result)

    return result

config = ConfigParser()
config.read('/config.ini')

_ACCOUNT = config['STOXXLOGIN']['ACCOUNT']
_PASSWORD = config['STOXXLOGIN']['PASSWORD']

var = '123'

result = requestlib()._requests(
                                'https://www.stoxx.com/documents/stoxxnet/Documents/Indices/Current/Composition_Files/opencomposition_sx50ul.csv',
                                _ACCOUNT,
                                _PASSWORD)

process_data = STOXX_DATA(result.text)
process_data.to_csv(
                    '/TODO_name_20240101.csv',
                    index = False)

# 這塊為了取得資料夾內所有檔案最新日期, 作為日期 ..

# os.chdir('/test')
# date = pd.DataFrame(os.listdir(),columns=['檔案名稱'])
# date1 = date.loc[date['檔案名稱'].str.contains(".csv")]
# date1 = date1.loc[date1['檔案名稱'].str.contains('TODO_name')]
# date2 = date1['檔案名稱'].str[-12:-4]
# date2 = pd.DataFrame(date2)
# date3 = date2.sort_values('檔案名稱',ascending=False).reset_index(drop=True)
# data_new = date3.iloc[0,0]

ConsData = pd.read_csv('/TODO_name_20240101.csv')
ConsCol = ConsData.columns[0].split(';')
ConsDataMerg = []
ConsDataMerg = pd.DataFrame(ConsDataMerg)
for i in range(0,ConsData.shape[0]):
    ConsDataTemp = pd.DataFrame(ConsData.iloc[:,0].str.split(';')[i]).transpose()
    # ConsDataMerg = ConsDataMerg.append(ConsDataTemp)
    ConsDataMerg = pd.concat([ConsDataMerg, ConsDataTemp])
ConsDataMerg.columns = ConsCol
ConsDataMerg = ConsDataMerg.reset_index(drop=True)
ConsDataMerg['tdate'] = pd.to_datetime('20240101')
ConsDataMerg['tdate'] = ConsDataMerg['tdate'].astype('str')

result = requestlib()._requests(
                                'https://www.stoxx.com/documents/stoxxnet/Documents/Indices/Current/HistoricalData/h_sx50ugv.txt',
                                _ACCOUNT,
                                _PASSWORD)

# TODO: STOXX_DATA() get Date / Indexvalue

result = requestlib()._requests(
                                'https://www.stoxx.com/documents/stoxxnet/Documents/Indices/Current/HistoricalData/h_sx50ul.txt',
                                _ACCOUNT,
                                _PASSWORD)

# TODO: STOXX_DATA() get Date / Indexvalue


# with open('/open_sx50ul_' + var + '.csv', 'wb') as f:
#     f.write(result.text)
    

# # 點擊登入
# driver.find_element_by_xpath("//input[@id='user-login']").click()
# time.sleep(1)

# # 切換 SX50UL網頁位置
# time.sleep(6)
# driver.get('https://www.stoxx.com/data-index-details?symbol=SX50UL')
# time.sleep(3)

# # 網頁連續向下滾動三次
# attempts = 1
# success = False
# while attempts < 3 and success == False:
#     try:
#         # 向下滾動
#         js="var action=document.documentElement.scrollTop=10000"
#         driver.execute_script(js)
#         success = True
#     except:
#         print("網頁向下滾動失敗")
#         attempts = attempts
#         time.sleep(3)
# time.sleep(3)

# # 點擊瀏覽美股歷史 USA500 － 異常重試 5 次 (需要再次確認)
# attempts = 1
# success = False
# while attempts < 6 and success == False:
#     try:
#         # 點擊瀏覽美股歷史 USA500
#         time.sleep(15)
#         driver.find_element_by_xpath("//a[contains(@href,'https://www.stoxx.com/documents/stoxxnet/Documents/Indices/Current/HistoricalData/h_sx50ul.txt')]").click()
#         time.sleep(1)
#         success = True
#         print('US500_history_success')
#     except:
#         print('US500_history_Error' + str(attempts))
#         attempts = attempts + 1
#         if attempts == 6:
#             break

# # 切換新視窗分頁，以讀取資料
# windows = driver.window_handles
# driver.switch_to.window(windows[-1])

# # 確認目前連結網頁
# print(driver.current_url)

# # 讀取目前連結網頁中 html語法 －　日期須調整
# html= driver.find_element_by_xpath(".//html")
# text = html.text

# # 分割文本資料
# textdata = text.split(';')
# textdata = pd.DataFrame(textdata)
# textdata.columns = ['text']

# # 抓取 US 500 最新日期及資料
# textfinaldata = textdata.iloc[textdata.shape[0]-2,0]
# textfinaldate = textdata.iloc[textdata.shape[0]-4,0]
# print(textfinaldata)

# text2 = textfinaldate[-4:] + textfinaldate[-7:-5] + textfinaldate[-10:-8]
# print(text2)

# #################### 判斷日期是否為整數型態 ####################
# try:
#     int(text2)
# except:
#     print('美國500大官網日期尚未更新')
#     int(text2)DailyUS500TRIdxStkTDHisClean.py

#                                    # 三、下載檔案
# # 切換回原始視窗介面，以下載檔案
# windows = driver.window_handles
# driver.switch_to.window(windows[0])

# ##################### 下載檔案 #####################
# # 點擊下載美股 USA500 － 異常重試 5 次
# attempts = 1
# success = False
# while attempts < 6 and success == False:
#     try:
#         # 點擊下鮺美股 USA500
#         time.sleep(15)
#         driver.find_element_by_xpath("//a[contains(@href,'https://www.stoxx.com/documents/stoxxnet/Documents/Indices/Current/Composition_Files/opencomposition_sx50ul.csv')]").click()
#         time.sleep(5)
#         success = True
#         print('US500_Download_success')
#     except:
#         print('US500_Download_Error' + str(attempts))
#         attempts = attempts + 1
#         if attempts == 6:
#             break
# driver.close()
# driver.quit()

#                                  # 四、整理下載檔案 (US500)
# # 整理 US500
# # 設定下載資料夾及設定操作介面 - 需要根據桌機調整
# target = 'W:/STOXX美股500ETF/指數下載'
# try:
#     os.chdir("C:/Users/setup/Downloads") 
#     # 重新命名檔案名稱
#     os.rename(src = 'opencomposition_sx50ul.csv', dst = 'open_sx50ul_'+text2+'.csv')
# except:
#     os.chdir("/Downloads")
#     # 重新命名檔案名稱
#     os.rename(src = 'opencomposition_sx50ul.csv', dst = 'open_sx50ul_'+text2+'.csv')
# # 移動檔案至指定位置
# shutil.move('_'+text2+'.csv',target)
