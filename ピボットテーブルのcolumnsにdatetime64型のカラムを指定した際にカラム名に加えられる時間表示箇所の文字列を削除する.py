import pandas as pd
# 横持データに変更
pivot_df =df.pivot_table(index=['勘定科目コード','勘定科目名'], columns='決算日', values='金額合計', aggfunc='sum')
# →datetime64型のカラムを列に指定するとカラム名が「2017-06-30 00:00:00」になってしまう

# 決算日の時間表示部分(2017-06-30 00:00:00の「00:00:00」)の文字列を削除
pivot_df = pivot_df.rename(columns = lambda x: str(x).split()[0])