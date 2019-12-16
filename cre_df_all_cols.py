import gc
import glob
import os
import sys

import pandas as pd
import numpy as np

def create_dataframe_about_columns_on_files(file_name_list, df_list):
    '''
    関数内容
    ・各ファイルのカラム名を1ファイルごとに抽出し、データフレームに格納する関数
    Input
    ・file_name_list：読み込みたいファイルの名前が格納されているリスト
    ・df_list：抽出したいカラムが含まれているデータフレームのリスト
    関数使用方法
    ・z_col_df = create_dataframe_about_columns_on_files(file_zaiko_name_list, df_list2)
    '''
    col_df_list = [pd.DataFrame({name:df.columns.tolist()}) for name, df in zip(file_name_list, df_list)]
    
    col_df = pd.concat(col_df_list, axis=1)
    
    return col_df
    

