import sys,os
import gc
from pathlib import Path
import glob
import re

import pandas as pd
import numpy as np


def draft_change_schema_in_sqlserver(sql_table_name_list):
    '''
    関数内容
    ・SQLServerにてテーブルのスキーマ名の変更(dbo→raw)を行うコードの下書きを表示する関数
    Input
    ・sql_table_name_list：変更したいテーブル名が格納されているリスト
    関数使用方法
     # テーブル名をリストに格納
     path = r'C:\Users\data'
     file_list = glob.glob(path + '\*.csv')
     file_list = sorted(file_list)
     file_name_list = [os.path.splitext(os.path.basename(file))[0] for file in file_list]
     # 関数の実行
     draft_change_schema_in_sqlserver(file_name_list)
    '''
    
    for name in sql_table_name_list:
        print('alter schema [raw] transfer [dbo].[' + name + ']')
    
    print('-'*70)
    print('下書きが完了しました。')