import sys,os
import gc
from pathlib import Path
import glob
import re


import pandas as pd
import numpy as np

# SQLserverへ接続開始する関数
def connect_to_sqlserver(database, driver='{SQL Server}', server = 'JPTOKCMZFDASQ01\INST1',trusted_connection='yes'):
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
    
    
    
# SQLserverへ接続開始する関数を実行
conn, curs = connect_to_sqlserver('Demo_FS')

# !!!データベース内のテーブルをデータフレームに変換し、それをリストに格納する関数!!!
pandas.read_sqlを利用
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql.html#pandas.read_sql
https://webcache.googleusercontent.com/search?q=cache:b05JZwp4_HIJ:https://ohke.hateblo.jp/entry/2017/06/30/230000+&cd=1&hl=ja&ct=clnk&gl=jp


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
    
# データベース内のテーブルをデータフレームに変換し、それをリストに格納する関数を実行
file_name_list = ['ana.財務諸表_PIVOT']
out_df_list = table_in_sqlserver_convert_to_dataframe(file_name_list)

# リストに格納したデータフレームの確認
for out_df in out_df_list:
    my_fda_functions.basic_check(out_df)
    display('-'*80)

# SQLserverへの接続を切る関数
def disconnect_from_sqlserver(curs=curs, conn=conn):
    '''
    関数内容
    ・SQLserverへの接続を切る関数
    '''
    curs.close()
    conn.close()
    

# SQLserverへの接続を切る関数を実行
disconnect_from_sqlserver()
