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
    
    
    df['diviation']  = abs(df[col] - np.mean(df[col],axis=0))
    df['3sigma'] = np.std(df[col],ddof=0,axis=0)*3
    
    return df

# ['diviation'] 、[3sigma]カラムを追加
df = get_diviation_and_3sigma(df,'_正規化_直前四半期差分')


# 平均値±3シグマ以上であれば「1」(全体の約99.7%の中に含まれていないので異常値である)、そうでなければ「0」（全体の約99.7%の中に含まれているので異常値ではない)と判定するカラムを追加
df['外れ値判定']=pt_df.apply(lambda x: 1 if x['diviation'] >= x['3sigma'] else 0, axis=1)
