import pandas as pd

# 作成するデータフレームが1行のみの場合は値をリストに格納する必要がある

pkl_out_df = pd.DataFrame({
    'データ件数':[pkl_df.shape[0]],
    '金額合計':[pkl_df['金額'].sum()],
    '単価合計':[pkl_df['単価'].sum()]
})