import pandas

df1 = df.copy()
df1['番号_文字数'] = df1['番号'].map(lambda x: len(x) if x!=None else np.nan)