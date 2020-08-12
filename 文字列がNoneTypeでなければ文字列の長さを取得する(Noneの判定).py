import pandas

df1 = df.copy()
df1['”Ô†_•¶š”'] = df1['”Ô†'].map(lambda x: len(x) if x!=None else np.nan)