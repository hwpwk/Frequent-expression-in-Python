import pandas as pd
import numpy as np

def getting_year_and_month_col(df, date_col='決算日'):
    '''
    関数内容
    ・決算年、決算月を取得する関数
    Input
    ・df：データフレーム
    ・date_col:決算日に相当するカラム
    '''
    
    # datetime型に変換
    df[date_col] = pd.to_datetime(df[date_col])
    # 決算年の取得
    df['year']=df[date_col].dt.year
    # 決算月の取得
    df['month']=df[date_col].dt.month
    
    return df

def create_fiscal_year_col(df, closing_month):
    '''
    関数内容
    ・決算月から四半期と会計年度を取得する関数
    Input
    ・df：データフレーム
    ・closing_month：決算月
    ・date_col：決算日に該当するカラム
    '''   
    
    # 四半期と会計年度の取得
    if closing_month <= 3:
        if df['month'] == int(closing_month):
            df['quarter']= 4
            df['fiscal_year'] = df['year']-1
        elif df['month'] == int(closing_month)+3:
            df['quarter']= 1
            df['fiscal_year'] = df['year']
        elif df['month'] == int(closing_month)+6:
            df['quarter']= 2
            df['fiscal_year'] = df['year']
        elif df['month'] == int(closing_month)+9:
            df['quarter']= 3
            df['fiscal_year'] = df['year']
            
    elif 4 <= closing_month <= 6:
        if df['month'] == int(closing_month):
            df['quarter']= 4
            df['fiscal_year'] = df['year']-1
        elif df['month'] == int(closing_month)+3:
            df['quarter']= 1
            df['fiscal_year'] = df['year']
        elif df['month'] == int(closing_month)+6:
            df['quarter']= 2
            df['fiscal_year'] = df['year']
        elif df['month'] == (int(closing_month)+9)-12:
            df['quarter']= 3
            df['fiscal_year'] = df['year']-1
        
    elif 7 <= closing_month <= 9:
        if df['month'] == int(closing_month):
            df['quarter']= 4
            df['fiscal_year'] = df['year']-1
        elif df['month'] == int(closing_month)+3:
            df['quarter']= 1
            df['fiscal_year'] = df['year']
        elif df['month'] == (int(closing_month)+6)-12:
            df['quarter']= 2
            df['fiscal_year'] = df['year']-1
        elif df['month'] == (int(closing_month)+9)-12:
            df['quarter']= 3
            df['fiscal_year'] = df['year']-1
    
    elif 10 <= closing_month:
        if df['month'] == int(closing_month):
            df['quarter']= 4
            df['fiscal_year'] = df['year']
        elif df['month'] == (int(closing_month)+3)-12:
            df['quarter']= 1
            df['fiscal_year'] = df['year']
        elif df['month'] == (int(closing_month)+6)-12:
            df['quarter']= 2
            df['fiscal_year'] = df['year']
        elif df['month'] == (int(closing_month)+9)-12:
            df['quarter']= 3
            df['fiscal_year'] = df['year']

    return df

def create_quarterly_col(df):
    '''
    関数内容
    ・四半期と会計年度を連結して四半期年度カラムを作成する関数
    Input
    ・df:データフレーム
    '''
    
    df = df.astype({'fiscal_year':str, 'quarter':str})
    
    df['四半期年度'] = df['fiscal_year']+'Q'+df['quarter']
    
    return df

# summary
def create_datafreme_about_adding_quarter_col(df, closing_month, date_col='決算日'):
    '''
    関数内容
    ・決算日と決算年、決算月、四半期、会計年度を取得して四半期年度カラムを作成しデータフレームを整理する関数
    Input
    ・df：データフレーム
    '''
    df = getting_year_and_month_col(df)

    df = df.apply(lambda x: create_fiscal_year_col(x, closing_month), axis=1)
    
    df = create_quarterly_col(df)

    return df