
import pandas as pd
import numpy as np
import openpyxl

# 空のエクセルファイルを作成(このファイルに新規データを書き込む)
out_path = r'C:/data/Excel/'

save_df = pd.DataFrame()
save_df.to_excel(out_path+'まとめ_201804.xlsx', index=False)

with pd.ExcelWriter(out_path+'日計データ_JOIN都道府県_まとめ(単位換算処理あり2)_20180401_20191231_インポートチェック_200217.xlsx', engine='openpyxl') as writer:
    writer.book = openpyxl.load_workbook(out_path+'日計データ_JOIN都道府県_まとめ(単位換算処理あり2)_20180401_20191231_インポートチェック_200217.xlsx')
    
    p_df.to_excel(writer, sheet_name='都道府県', index=False)
    r_df1.to_excel(writer, sheet_name='地方名_分類1', index=False)
    r_df2.to_excel(writer, sheet_name='地方名_分類2', index=False)


# 参考：https://note.nkmk.me/python-pandas-to-excel/
# エラー対処参考：https://stackoverflow.com/questions/49519696/getting-attributeerror-workbook-object-has-no-attribute-add-worksheet-whil

