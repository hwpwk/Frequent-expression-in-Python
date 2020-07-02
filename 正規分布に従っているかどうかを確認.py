import pandas as pd
import numpy as np

# ヒストグラムの描画
df['_正規化'].hist()

# 正規Q-Qプロットによる可視化
from scipy import stats
stats.probplot(df['_正規化'], dist='norm', plot=plt)

# シャピロウィルク検定(欠損値があるとWがnan、P値が1になるので欠損値を補完してから使用する)
from scipy import stats
W, p = stats.shapiro(df['_正規化'])
print( 'p値 = ', p)

