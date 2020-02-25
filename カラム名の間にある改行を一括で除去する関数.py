import pandas as pd
import numpy as np


def trim_new_lines_from_colmuns(df):
    '''
    関数内容
    ・カラム名の間にある改行を一括で除去する関数
    Input
    ・df：データフレーム
    関数使用方法
    df_list2 =[trim_new_lines_from_colmuns(df) for df in df_list]
    '''
    
    df = df.rename(columns=lambda x: x.replace('\n',''))
    
    return df