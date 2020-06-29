import pandas as pd
import numpy as np


# intやfloatなどの数値型のカラムのみ抽出
value_col_list = tmp_df2.select_dtypes(include=['number']).columns.tolist()

# データフレームから値がinfとなっているレコードを抽出
df[np.isinf(df[value_col_list]).any(1)]