﻿# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


def create_basic_dataframe2(database, query):
    
    '''
    関数内容
    ・SQLserverの指定データベースに接続し指定テーブルから会社名、決算日、各会計指標を抽出&追加する関数
    Input
    ・database:接続したいデータベース名
    ・query：SQLコード
    関数使用方法
    ・df = create_basic_dataframe2('C210xx',query)
    '''
    
    # 1.SQLserverの指定データベースに接続を開始する関数
    conn, curs = connect_to_sqlserver2(database)
    # 2.データベース内のテーブルをデータフレームに変換する関数
    df = table_in_sqlserver_convert_to_dataframe2(query, conn)
    # 3.SQLserverへの接続を切る関数
    disconnect_from_sqlserver(curs, conn)
    
    return df
 
# 1    
def connect_to_sqlserver2(database, driver='{ODBC Driver 17 for SQL Server}', server = 'xxxxxx',trusted_connection='yes'):
    '''
    関数内容
    ・PythonからSQLserverへ接続する関数
    Input
    ・database：使用するデータベース名(予めSQLserver上で「CREATE DATABASE [データベース名]」というコードを実行させて作成しておく)
    関数使用方法
    ・connect_to_sqlserver('C_database')
    '''
    import pyodbc
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';Trusted_Connection='+trusted_connection+';')
    curs = conn.cursor()
    
    return conn, curs
    
# 2
def table_in_sqlserver_convert_to_dataframe2(query,conn):
    '''
    関数内容
    ・データベース内のテーブルをデータフレームに変換する関数
    Input
    ・table_name：抽出したいテーブルの名前
    関数使用方法
    query='SELECT * FROM tbl'
    df = table_in_sqlserver_convert_to_dataframe2(query,conn)
    '''
    df = pd.read_sql(sql=query +';', con=conn)
    
    return df
# 3
def disconnect_from_sqlserver(curs, conn):
    '''
    関数内容
    ・SQLserverへの接続を切る関数
    '''
    curs.close()
    conn.close()