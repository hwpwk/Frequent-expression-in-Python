import pandas as pd
import numpy as np

def add_fiscal_year_col_to_dataframe(df, closing_month):
    '''
    関数内容
    ・データフレームに会計年度カラム(期の始まりの年月が属する暦年を会計年度とする)を追加する関数
    Input
    ・df:データフレーム
    ・closing_month:決算月
    関数使用方法
     df1 = add_fiscal_year_col_to_dataframe(tmp_df1, 3)
    '''
    from dateutil.relativedelta import relativedelta

    # 決算日から決算月の12の剰余を引く
    df['会計年度_tmp'] = df['決算日'].map(lambda x:x-relativedelta(months=closing_month%12))
    
    # 会計年度の抽出
    df['会計年度'] = df['会計年度_tmp'].dt.year
    
    # 必要のないカラムを削除
    df = df.drop('会計年度_tmp', axis=1)
    
    return df


def add_usa_fiscal_year_col_to_dataframe(df, closing_month):
    '''
    関数内容
    ・データフレームに会計年度カラム(締めの年月が属する暦年を会計年度とする)を追加する関数
    Input
    ・df:データフレーム
    ・closing_month:決算月
    関数使用方法
     df1 = add_fiscal_year_col_to_dataframe(tmp_df1, 3)
    '''
    from dateutil.relativedelta import relativedelta

    # 決算日から決算月の12の剰余を引く
    df['会計年度_tmp'] = df['決算日'].map(lambda x: x-relativedelta(months=closing_month%12))
    
    # 会計年度の抽出(決算月が12月か12月以外かで処理を分岐)
    if closing_month != 12:
        df['会計年度'] = df['会計年度_tmp'].dt.year + 1
    else:
        df['会計年度'] = df['会計年度_tmp'].dt.year
    
    # 必要のないカラムを削除
    df = df.drop('会計年度_tmp', axis=1)
    
    return df
