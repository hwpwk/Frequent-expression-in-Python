import pandas as pd
import numpy as np

def calc_cost_of_sales_ratio(numerator_col, denominator_col):
    '''
    関数内容
    ・売上原価率(単位:パーセント)を算出する関数(分母が0であるかそうでないかで処理方法を変えている)
    Input
    ・numerator_col:分子にしたいカラム
    ・denominator_col:分母にしたいカラム
    関数使用方法
　　df['売上原価率'] = df1.apply(lambda x: calc_cost_of_sales_ratio(x['売上原価'],x['売上高']), axis=1)
    '''
    # 分母が0の場合
    if denominator_col == 0:
        cost_of_sales_ratio = 0
    
    # 分母が0以外の場合
    else:
        cost_of_sales_ratio = round((numerator_col / denominator_col), 3)*100
        
    return cost_of_sales_ratio