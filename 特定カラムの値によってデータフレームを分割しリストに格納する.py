import pandas as pd
# ファイル名によってデータフレームを分割しリストに格納
file_df_list = [df.groupby('ファイル名').get_group(name) for name, group in df.groupby('ファイル名')]