import pandas

# 複数カラムの値を連結したいとき、

df['new_col'] = df['区分']+df['コード']+df['テキスト']

'''
上記のような複数カラムの値を連結するコードを実行した際に
「TypeError: ufunc 'add' did not contain a loop with signature matching types dtype('<U21') dtype('<U21') dtype('<U21')」
というエラーが発生した場合には下記を実行する。
'''
df['new_col'] = df[['区分','コード','テキスト']].apply(lambda x: '{}{}{}'.format(x['区分'],x['コード'],x['テキスト']),axis=1)

参考： https://www.kato-eng.info/entry/pandas-concat-pk

