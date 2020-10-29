import pandas as pd
import numpy as np

# 決算日カラムをdatetime型に変換
tmp_df['決算日'] = pd.to_datetime(tmp_df['決算日'])

# 基準日から3か月前の日付を算出
from dateutil import relativedelta
tmp_df['-1Q決算日'] = tmp_df['決算日'].map(lambda x: x - relativedelta.relativedelta(months=3))


def add_closing_date_col(df, raw_date_col='日付', col2='決算年', col3='前決算月', col4='決算月_月末日', col5='前決算日'):
    '''
     月末日を算出する関数
    
    '''
    # raw_date_colの値が「201706」のような6文字の場合に使える
    df[col2] = df[raw_date_col].apply(lambda x: str(x)[0:4])
    df[col3] = df[raw_date_col].apply(lambda x: str(x)[4:])

    import calendar
    df = df.astype({col2:int, col3:int})
    df[col4] = df.apply(lambda x: calendar.monthrange(x[col2], x[col3])[1], axis=1)

    df = df.astype({col2:str, col3:str, col4:str})
    df[col3] = df[col3].apply(lambda x: x.zfill(2))

    df[col5] = df[col2] + df[col3] + df[col4]

    df[col5] = pd.to_datetime(df[col5], format='%Y-%m-%d')
    
    return df

# 上記処理のみでは3月は30日になるので月末日になるようにする

# str型にする
tmp_df['-1Q決算日str'] = tmp_df['-1Q決算日'].map(lambda x: x.strftime('%Y/%m/%d'))

# 201512の形にする
tmp_df['日付'] = tmp_df['-1Q決算日str'].map(lambda x: x[0:4]) + tmp_df['-1Q決算日str'].map(lambda x: x[5:7])

# 月末日を算出する関数
tmp_df = add_closing_date_col(tmp_df)

## →前期の決算日の作成が完了


