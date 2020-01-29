import pandas

# 計上日は昇順で、数量は降順で同時に並べ替えたいとき
df.groupby(['計上日','都道府県'])['数量'].sum().reset_index().sort_values(['計上日','数量'], ascending=[True,False])