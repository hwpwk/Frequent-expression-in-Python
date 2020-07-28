import pandas as pd
# agカラム、stカラムのどちらかが欠損値になっているレコードを削除
df = df.dropna(subset=['ag', 'st'])

# agカラム、stカラムのどちらも欠損値になっているレコードを削除
df = df.dropna(subset=['ag', 'st'], how='all')