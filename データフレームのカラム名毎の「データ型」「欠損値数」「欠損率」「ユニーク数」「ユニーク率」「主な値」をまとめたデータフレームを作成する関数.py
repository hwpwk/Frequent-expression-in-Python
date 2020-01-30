import gc
import glob
import os
import sys

import pandas as pd
import numpy as np


def col_data_in_dataframe2(df):
    '''
    関数内容
    ・データフレームのカラム名毎の「データ型」「欠損値数」「欠損率」「ユニーク数」「ユニーク率」「主な値」をまとめたデータフレームを作成する関数
    Input
    ・df：データフレーム
    関数使用方法
    ・col_data_in_dataframe2(df)
    '''
    
    col_list = df.columns.tolist()
    null_num_list = df.isnull().sum().tolist()
    data_type_list = df.dtypes.tolist()
    col_unique_num_list = df.nunique().tolist()
    null_num_per_list = [str(round(num/df.shape[0],2)*100)+'%' for num in null_num_list]
    unique_num_per_list = [str(round(num/df.shape[0],2)*100)+'%' for num in col_unique_num_list]
    main_values_list = [df[col].value_counts().reset_index()['index'].tolist()[:3] for col in df.columns.tolist()]

    summary_df = pd.DataFrame({
        'カラム名':col_list,
        'データ型':data_type_list,    
        '欠損値数':null_num_list,
        '欠損率':null_num_per_list,
        'ユニーク数':col_unique_num_list,
        'ユニーク率':unique_num_per_list,
        '主な値':main_values_list
    })

    return summary_df