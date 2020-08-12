
import pandas as pd
import numpy as np


def create_basic_dataframe(database, table_name):
    
    '''
    関数内容
    ・SQLserverの指定データベースに接続し指定テーブルすべてのデータを抽出する関数
    Input
    ・database:接続したいデータベース名
    ・table_name：抽出したいテーブルの名前
    関数使用方法
    ・df = create_basic_dataframe()
    '''
    
    # 1.SQLserverの指定データベースに接続を開始する関数
    conn, curs = connect_to_sqlserver(database)
    # 2.データベース内のテーブルをデータフレームに変換する関数
    df = table_in_sqlserver_convert_to_dataframe2(table_name, conn)
    # 3.SQLserverへの接続を切る関数
    disconnect_from_sqlserver(curs, conn)
    
    return df
 
# 1    
def connect_to_sqlserver(database, driver='{SQL Server}', server = 'xx1',trusted_connection='yes'):
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
# 2
def table_in_sqlserver_convert_to_dataframe2(table_name, conn):
    '''
    関数内容
    ・データベース内のテーブルをデータフレームに変換する関数
    Input
    ・table_name：抽出したいテーブルの名前
    関数使用方法
    
    '''
    query = '''
     SELECT
         *
     FROM 
    '''
    
    df = pd.read_sql(sql=query + table_name +';', con=conn)
    
    return df
# 3
def disconnect_from_sqlserver(curs, conn):
    '''
    関数内容
    ・SQLserverへの接続を切る関数
    '''
    curs.close()
    conn.close()
