import pandas as pd
# 重複するカラム名を削除
df = df.loc[:,~df.columns.duplicated()]