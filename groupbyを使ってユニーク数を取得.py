import pandas as pd

# 決算日毎の会社のユニーク数を取得
df.groupby('決算日')[['会社']].nunique()