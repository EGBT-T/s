import os
from datetime import datetime

import pandas as pd
from ftplib import FTP
from opencc import OpenCC

converter = OpenCC('s2t.json')

ftp = FTP()
ftp.set_pasv(1)
bufsize = 1024

ftp.connect('WEB', port=20021)
ftp.login(user='user', passwd='passwd')

# ftp.cwd('CHANGE PATH')
# ftp.retrbinary("RETR {}".format('CW'), \
#                open('DOWNLOAD PATH ~ CW FILE', 'wb').write, bufsize)

# ftp.cwd('CHANGE PATH')
# ftp.retrbinary("RETR {}".format('CA'), \
#                open('DOWNLOAD PATH ~ CA FILE', 'wb').write, bufsize)

# ftp.cwd('CHANGE PATH')
# ftp.retrbinary("RETR {}".format('div'), \
#                open('DOWNLOAD PATH ~ DIV FILE', 'wb').write, bufsize)

# ftp.cwd('CHANGE PATH')
# ftp.retrbinary("RETR {}".format('WND'), \
#                open('DOWNLOAD PATH ~ WND FILE', 'wb').write, bufsize)

# ftp.cwd('CHANGE PATH')
# ftp.retrbinary("RETR {}".format('AS_P'), \
#                open('DOWNLOAD PATH ~ AS_P FILE', 'wb').write, bufsize)

# ----- SPLIT -----

# abc = pd.read_excel('WND', dtype=object)

# abc_json = abc.to_json(force_ascii=False)
# abc_json_convert = converter.convert(abc_json)
# abc_json_convert_df = pd.read_json(abc_json_convert, dtype=object)
# abc_json_convert_df.to_csv('abc_json_convert_df.csv', encoding='utf_8_sig')

# abc_json_convert_df.columns = [...]

# abc_json_convert_df['tdate'] = 'Dt'

# abc_json_convert_df.to_sql('SQL_TABLE', con='SQL_CONNECstr', if_exists='append', index=False)

# ----- SPLIT -----

# _SQL_QUERY = pd.read_sql('QUERY_STR', con='SQL_CONNECstr')
# sql_CSII = "SELECT * FROM 'TABLE' WHERE idxid = 'SYM' AND tdate ='" + date_new + "'"

# _SQL_QUERY = pd.read_sql('QUERY_STR', con='SQL_CONNECstr')
# sql_date = "SELECT DISTINCT tdate FROM 'TABLE' WHERE idxid = 'SYM' ORDER BY tdate DESC"

# ----- SPLIT -----

# abc_json_convert_df['ticker'] = abc_json_convert_df['stkid']
# abc_json_convert_df.loc[abc_json_convert_df[''] == '', ''] = abc_json_convert_df.loc[abc_json_convert_df[''] == '', ''] + ' '
# abc_json_convert_df.loc[abc_json_convert_df[''] == '', ''] = abc_json_convert_df.loc[abc_json_convert_df[''] == '', ''] + ' '
# abc_json_convert_df['totmv'] = abc_json_convert_df['totmv'] / 1000000
# abc_json_convert_df = abc_json_convert_df[...]
# abc_json_convert_df.to_sql('SQL_TABLE', con='SQL_CONNECstr', if_exists='append', index=False)

# ----- SPLIT -----

# COL_LIST = [...]
# abc_txt = pd.read_csv('AS_P', sep='\s*[|]', skiprows=23, names=COL_LIST, usecols=COL_LIST, engine='python')
# abc_txt = abc_txt[abc_txt['idxid'] == 'SYM'].loc[:, ~abc_txt.columns.str.contains('point')]
# abc_txt.to_sql('SQL_TABLE', con='SQL_CONNECstr', if_exists='append', index=False)
