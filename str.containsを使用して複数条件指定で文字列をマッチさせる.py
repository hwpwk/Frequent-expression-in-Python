import pandas as pd

# カラム名先頭がアルファベットかUnnamedのカラムを削除し、それ以外のカラムを抽出したい
# df:カラム名「a」、「b」、「Unnamed：33」などが含まれているデータフレームとする

use_cols=df.columns[~df.columns.str.contains('^[a-zA-Z]|Unnamed:')]
df1 = df[use_cols]

# 参考
# Unnamed:関連のカラムを削除：https://tutorialmore.com/questions-1586224.htm
# 複数条件指定で文字列をマッチさせるhttps://blog.pyq.jp/entry/python_kaiketsu_181031