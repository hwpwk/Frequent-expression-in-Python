import pandas as pd
# 名の全角スペースと半角スペースを削除
# 「'NoneType' object has no attribute 'replace'」というエラーが発生しないよう条件式if x!=Noneを追加
# https://support.esri.com/ja/technical-article/000014467
df['_修正'] = df['名'].map(lambda x: x.replace(' ','').replace('　','') if x!=None else x)