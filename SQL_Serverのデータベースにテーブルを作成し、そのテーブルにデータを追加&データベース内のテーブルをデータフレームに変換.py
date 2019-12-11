# coding: utf-8

# In[1]:
import sys,os
import gc
from pathlib import Path
import glob
import re
import pickle
import warnings
import re

import pandas as pd
import numpy as np

## 指定ディレクトリに格納されているcsvファイルのパスを取得
# In[8]:
path = r'C:\Users\data'
file_list = glob.glob(path + '\*表*.csv')
file_list

## データフレームとして読み込みリストに格納
# この際、カラムの順序を指定する

# In[9]:
# カラムの順序を指定
order_cols = ['決算日',  'B/C', 'コード', '金額']

# In[10]:


# int型で指定した場合、欠損値があるとエラーになるのですべてのカラムをstr型で読み込む
df_list =[pd.read_csv(file, encoding='ms932',engine='python',dtype='object') for file in file_list]

# カラムの順序を指定順に変更
df_list = [df[order_cols] for df in df_list]

# 欠損値があればNoneを補完
df_list = [df.where(df.notnull(), None) for df in df_list]

for df in df_list:
    display(df.head(10))


# In[12]:


# 読み込んだデータフレームの各カラムのデータ型の確認
for df in df_list:
    display(df.shape, df.dtypes)


# ## SQLserverへ接続開始する関数

# In[13]:

def connect_to_sqlserver(database, driver='{SQL Server}', server = 'localhost\SQLEXPRESS',trusted_connection='yes'):
    '''
    関数内容
    ・PythonからSQLserverへ接続する関数
    Input
    ・database：使用するデータベース名(予めSQLserver上で「CREATE DATABASE [データベース名]」というコードを実行させて作成しておく)
    関数使用方法
    ・connect_to_sqlserver('C10000_database')
    '''
    import pyodbc
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';Trusted_Connection='+trusted_connection+';')
    curs = conn.cursor()
    
    return conn, curs


# ### SQLserverへ接続開始する関数を実行

# In[14]:

conn, curs = connect_to_sqlserver('test_db_1')


# ## データベース内にテーブルを作成する関数¶
# 参考：https://itsakura.com/python-sqlite-insert

# In[15]:


def create_tables_in_sqlserver(file_name_list, curs=curs, conn=conn):
    '''
    関数内容
    ・データベース内にテーブルを作成する関数
    (カラムは[決算日]、[B/C]、[コード]、[金額]で決め打ち)
    Input
    ・file_name_list：読み込んだ全ファイル名を格納したリスト
    関数使用方法
    ・create_tables(file_name_list)
    '''
    # [/](スラッシュ)がカラム名に含まれている場合はカラム名を[]で囲う必要がある
    # NUMERICの最大指定桁数は38
    for file_name in file_name_list:
        print(file_name + 'のテーブルの作成を開始します。')
        curs.execute(
        'CREATE TABLE ' + file_name +\
        '(決算日 DATE,[B/C] VARCHAR(255),コード NVARCHAR(255),金額 FLOAT)')

        conn.commit()


# In[16]:
# ディレクトリに格納されているファイルの名前のみ取得
file_name_list = [os.path.splitext(os.path.basename(file))[0] for file in file_list]
file_name_list


# ### データベース内にテーブルを作成する関数を実行
# In[17]:
create_tables_in_sqlserver(file_name_list)

# ## データベース内のテーブルにデータを追加する関数

# In[18]:

def insert_into_sqlserver(file_name_list, df_list, curs=curs, conn=conn):
    '''
    関数内容
    ・データベース内のテーブルにデータを追加する関数
    Input
    ・file_name_list：読み込んだ全ファイル名を格納したリスト
    ・df_list：読み込んだ全データフレームを格納したリスト
    関数使用方法
    ・insert_into_sqlserver(file_name_list, df_list)
    
    '''
    for file_name, df in zip(file_name_list, df_list):
        values_tuple = [tuple(row) for row in df.values]
        print(file_name + 'のテーブルにデータを格納していきます。')
        # カラムが複数ある結果、挿入したい値が複数ある場合はcurs.executemanyを使う
        curs.executemany(
            'INSERT INTO ' + file_name +'(決算日, [B/C], コード, 金額) VALUES (?,?,?,?)',values_tuple
        )

        conn.commit()

# ### データベース内のテーブルにデータを追加する関数を実行

# In[19]:


insert_into_sqlserver(file_name_list, df_list)

### 追加(191205)

## データベース内のテーブルをデータフレームに変換し、それをリストに格納する関数

'''
pandas.read_sqlを利用

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql.html#pandas.read_sql

https://webcache.googleusercontent.com/search?q=cache:b05JZwp4_HIJ:https://ohke.hateblo.jp/entry/2017/06/30/230000+&cd=1&hl=ja&ct=clnk&gl=jp
'''

def table_in_sqlserver_convert_to_dataframe(file_name_list, conn=conn):
    '''
    関数内容
    ・データベース内のテーブルをデータフレームに変換し、それをリストに格納する関数
    Input
    ・file_name_list：読み込んだ全ファイル名を格納したリスト
    関数使用方法
    out_df_list = table_in_sqlserver_convert_to_dataframe(file_name_list)
　　 # リストに格納されているデータフレームの基本情報を順に確認する
    for out_df in out_df_list:
        my_fda_functions.basic_check(out_df)
        display('-'*80)
    '''
    
    out_df_list = [pd.read_sql(sql='SELECT * FROM ' + file_name +';', con=conn) for file_name in file_name_list]
    
    return out_df_list
    
### データベース内のテーブルをデータフレームに変換し、それをリストに格納する関数を実行
out_df_list = table_in_sqlserver_convert_to_dataframe(file_name_list)

for out_df in out_df_list:
    my_fda_functions.basic_check(out_df)
    display('-'*80)



# ## SQLserverへの接続を切る関数

# In[20]:


def disconnect_from_sqlserver(curs=curs, conn=conn):
    '''
    関数内容
    ・SQLserverへの接続を切る関数
    '''
    curs.close()
    conn.close()


# 
# ### SQLserverへの接続を切る関数を実行

# In[21]:


disconnect_from_sqlserver()


# 参考
# 
# https://qiita.com/gaborotta/items/3f2f2fd492163a1ec007
# 
# https://qiita.com/YoshitakaOkada/items/d6d97c5954adae148b7a
