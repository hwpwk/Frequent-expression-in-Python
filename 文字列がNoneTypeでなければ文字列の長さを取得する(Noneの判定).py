import pandas

df1 = df.copy()
df1['�ԍ�_������'] = df1['�ԍ�'].map(lambda x: len(x) if x!=None else np.nan)