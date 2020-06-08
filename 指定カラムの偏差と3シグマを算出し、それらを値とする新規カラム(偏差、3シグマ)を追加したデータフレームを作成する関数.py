import pandas as pd
import numpy as np

def get_diviation_and_3sigma(df, col):
    '''
    関数内容
    ・指定カラムの偏差と3シグマを算出し、それらを値とする新規カラム(偏差、3シグマ)を追加したデータフレームを作成する関数
    Input
    ・df:データフレーム
    ・col:偏差と3シグマを算出したいカラム
    関数使用方法
    　outlier_df10 = get_diviation_and_3sigma(outlier_df10, 'max')
    '''
    
    
    df['diviation'] = abs(df[col] - np.mean(df[col],axis=0))
    df['3sigma'] = np.std(df[col],ddof=0,axis=0)*3
    
    return df