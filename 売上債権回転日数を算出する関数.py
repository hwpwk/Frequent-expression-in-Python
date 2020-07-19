import pandas as pd
import numpy as np

def calc_accounts_receivable_turnover_period(numerator_col, denominator_col, day_col):
    '''
    関数内容
    ・売上債権回転日数を算出する関数(分母が0であるかそうでないかで処理方法を変えている)
    引数一覧
    ・numerator_col:分子にしたいカラム
    ・denominator_col:分母にしたいカラム
    ・day_col:期間(日数)として使いたい関数
    関数使用方法
    　df['売上債権回転日数']=df.apply(lambda x: calc_accounts_receivable_turnover_period(x['売上債権'],x['(期間)売上高'],x['四半期日数']), axis=1)
    '''
    
    # 分母が0の場合
    if denominator_col == 0:
        accounts_receivable_turnover_period = 0
    
    # 分母が0以外の場合
    else:
        accounts_receivable_turnover_period = round((numerator_col / denominator_col)*day_col, 3)
        
    return accounts_receivable_turnover_period