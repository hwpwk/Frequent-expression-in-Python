import pandas as pd
import numpy as np

def calc_zscore(x, ddof=0):
    '''
    関数内容
    　・z-score(元データを平均0、標準偏差を1に変換)を算出する関数
    Input
    　・x：数値データ(シリーズ型のデータ)
    　・ddof：母標準偏差を使用する場合は「0」、標本標準偏差を使用する場合は「1」
    関数使用方法
    　・df1['(期間)売上高_標準化'] = df1.groupby('会社コード')['(期間)売上高'].apply(lambda x: calc_zscore(x))
    '''
    
    x_mean = np.mean(x)# 平均
    x_std  = np.std(x,ddof=ddof)# 標準偏差

    zscore = (x - x_mean) / x_std
    
    return zscore

def calc_zscore2(x, ddof=0):
    '''
    関数内容
    　・z-score(元データを平均0、標準偏差を1に変換)を算出する関数
    Input
    　・x：数値データ(シリーズ型のデータ)
    　・ddof：母標準偏差を使用する場合は「0」、標本標準偏差を使用する場合は「1」
    関数使用方法
    　・df1['(期間)売上高_標準化'] = df1.groupby('会社コード')['(期間)売上高'].apply(lambda x: calc_zscore(x)) 
    '''
    
    x_mean = x.mean()# 平均
    x_std  = x.std(ddof=ddof)# 標準偏差

    zscore = (x - x_mean) / x_std
    
    return zscore
