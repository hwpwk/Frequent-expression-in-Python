import pandas as pd

# カラム名先頭が「*」、「＊」のカラムを削除しそれ以外のカラムを抽出したい
# str.containsを使用する場合、「*」、「＊」のようなメタ文字は記号の前に「\」を加える必要あり

all_zaiko_df.columns[~all_zaiko_df.columns.str.contains('\*|\＊')]