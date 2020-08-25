import pandas as pd

for col in df.columns.tolist():
    print('【'+str(col)+'】')
    display(df[col].value_counts().reset_index()[0:5])
    print('+'*70)