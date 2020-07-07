import pandas as pd
import numpy as np

# 下記3つのカラムをdatetime64型に変換
date_col = ['作業開始年月日','決算年月日', '引渡年月日']
for col in date_col:
    df[col] = pd.to_datetime(df[col])

# 日付の差分を取得
df['diff'] = (df['決算年月日']-df['作業開始年月日(商談単位の最小)']).dt.days