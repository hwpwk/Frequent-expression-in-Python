import pandas as pd
import numpy as np

# SQLServerにインポートするカラムをデータ型毎に分ける
date_col_list = ['月末日']
nvarchar_col_list = ['部門コード', '本部コード'']
numeric_col_list = ['契約金額', '合計金額']

# SQLServerにインポートする関数一式
def main_import_data_to_sqlserver(database,df,file_name,date_col_list,nvarchar_col_list,numeric_col_list):
    '''
    関数内容
    ・予め読み込んだデータをSQLServerにインポートする関数
    Input
    ・database：テーブルをインポートしたいデータベース名
    ・df：インポートしたいテーブル(データフレーム)
    ・file_name:インポートしたいテーブルの名前
    ・date_col_list：DATE型としてインポートしたいカラム名を格納したリスト
    ・nvarchar_col_list：NVARCHAR型としてインポートしたいカラム名を格納したリスト
    ・numeric_col_list：NUMERIC型としてインポートしたいカラム名を格納したリスト
    関数使用方法
    for df, file_name in zip(df_list1, file_name_list):
        main_import_data_to_sqlserver('210_tbl',df,file_name,date_col_list,nvarchar_col_list,numeric_col_list)
    '''
    # 1
    dtypes_df = extract_colname_and_dtype_from_dataframe(df,date_col_list,nvarchar_col_list,numeric_col_list)
    # 2
    conn, curs = connect_to_sqlserver(database)
    # 3
    colname_and_dtype_str = get_colname_and_dtype_to_create_table(dtypes_df)
    # 4
    create_tables_in_sqlserver(file_name, colname_and_dtype_str, curs=curs, conn=conn)
    # 5
    it_col_str, questionmark_str = get_colname_and_questionmark_to_insert_data(dtypes_df)
    # 6
    insert_into_sqlserver(file_name, df, it_col_str, questionmark_str,curs=curs, conn=conn)
    # 7
    disconnect_from_sqlserver(curs=curs, conn=conn)


# 1
def extract_colname_and_dtype_from_dataframe(df,date_col_list,nvarchar_col_list,numeric_col_list):
    '''
    関数内容
    ・読み込んだデータのカラム名とデータ型を抽出し、データ型はSQLServerへのインポート用のデータ型名に変換してそれらをデータフレームに格納する関数
    '''
    dtypes_df = pd.DataFrame(df.dtypes).reset_index()
    dtypes_df.columns=['カラム名','データ型']

    for i in range(len(dtypes_df)):
        if dtypes_df.loc[i,'カラム名'] in date_col_list:
            dtypes_df.loc[i,'データ型'] = 'DATE'
        elif dtypes_df.loc[i,'カラム名'] in nvarchar_col_list:
            dtypes_df.loc[i,'データ型'] = 'NVARCHAR(255)'
        elif dtypes_df.loc[i,'カラム名'] in numeric_col_list:
            dtypes_df.loc[i,'データ型'] = 'NUMERIC(25,2)'
        else:
            pass
    

    return dtypes_df

# 2
def connect_to_sqlserver(database, driver='{SQL Server}', server = 'xxxxx',trusted_connection='yes'):
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

# 3
def get_colname_and_dtype_to_create_table(df):
    '''
    関数内容
    ・create tableに必要なカラム名とデータ型を取得し、2つを特定の形式に並べた文字列を作成する関数
    '''

    ct_col_list = df['カラム名'].tolist()
    # カラム名に'/'が含まれているとSQLServerへのインポート時にエラーが発生するのでリネーム
    ct_col_list =['['+ col_name + ']' if '/' in col_name else col_name for col_name in ct_col_list]
    # カラム名先頭が数字の場合もSQLServerへのインポート時にエラーが発生するのでリネーム
    ct_col_list =['['+ col + ']' if re.match('^[0-9]', col) else col for col in ct_col_list ]

    ct_dtype_list = df['データ型'].tolist()

    combi_ct_list = [str(col_name)+' '+str(dtype_name) for col_name, dtype_name in zip (ct_col_list, ct_dtype_list)]

    colname_and_dtype_str = ','.join(map(str, combi_ct_list))

    return colname_and_dtype_str

# 4
def create_tables_in_sqlserver(file_name, colname_and_dtype_str, curs, conn):
    '''
    関数内容
    ・データベース内にテーブルを作成する関数
    '''
    #for file_name in file_name_list:
    
    print(file_name+'テーブルをSQLServerに作成します。')
    #print(colname_and_dtype_str)
    curs.execute(
    'CREATE TABLE ' + file_name +\
    '(' + colname_and_dtype_str +')')
    print(file_name+'テーブルをSQLServerに作成し終えました。')

    conn.commit()

# 5       
def get_colname_and_questionmark_to_insert_data(df):
    '''
    関数内容
    ・insert intoに必要なカラム名と?マークを取得する関数

    '''
    
    it_col_list = df['カラム名'].tolist()
    # カラム名に'/'が含まれているとSQLServerへのインポート時にエラーが発生するのでリネーム
    it_col_list =['['+ col_name + ']' if '/' in col_name else col_name for col_name in it_col_list]
    # カラム名先頭が数字の場合もSQLServerへのインポート時にエラーが発生するのでリネーム
    it_col_list =['['+ col + ']' if re.match('^[0-9]', col) else col for col in it_col_list ]

    it_col_str = ','.join(map(str, it_col_list))

    questionmark_str = '?,'*len(df)
    # 最後の「,」は必要ない + ()を追加
    questionmark_str = '(' + questionmark_str[:-1] + ')'

    return it_col_str, questionmark_str

# 6
def insert_into_sqlserver(file_name, df, it_col_str, questionmark_str, curs, conn):
    '''
    関数内容
    ・データベース内のテーブルにデータを追加する関数

    '''

    #for file_name, df in zip(file_name_list, df_list):
    
    print(file_name+'テーブルにデータを格納します。')
    
    values_tuple = [tuple(row) for row in df.values]
    # カラムが複数ある結果、挿入したい値が複数ある場合はcurs.executemanyを使う
    curs.executemany(
        'INSERT INTO ' + file_name +'(' + it_col_str + ')'+ 'VALUES ' + questionmark_str ,values_tuple
    )
    print(file_name+'テーブルにデータを格納し終えました。')

    conn.commit()

# 7
def disconnect_from_sqlserver(curs, conn):
    '''
    関数内容
    ・SQLserverへの接続を切る関数
    '''
    #conn, curs = connect_to_sqlserver()

    curs.close()
    conn.close()

