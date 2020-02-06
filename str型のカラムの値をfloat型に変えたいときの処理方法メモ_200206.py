import sys,os
import gc
import glob
import pandas as pd

files = glob.glob(r'L:/data/csv/*sale*')
files = sorted(wbs_files)

file_name_list = [os.path.splitext(os.path.basename(file))[0] for file in files]

df_list = [pd.read_csv(file,usecols=['売上'],encoding='cp932', engine='python') for file in files]


'''
以降、[売上]カラムの値を算出したいが[売上]カラムの値の1つに「8,400.00」といったカンマが入ってしまっている場合を想定する。
このとき、pandas.read_csvの引数に「dtype=float」と与えて[売上]カラムのデータ型をfloat型に変換しようとすると
「unable to convert column to type class 'float'」というエラーが発生してしまう可能性や、
[売上]カラムをstring型で読み込んだ後に
df['売上'] = df['売上'].apply(lambda x: x.replace(',','').astype(float))
という処理でデータ型をfloat型に変換しようとすると
「'str' object has no attribute 'astype'」というエラーが発生してしまう可能性がある。
このような場合には、str型からDecimal型にしてその後にfloat型に変換する処理を行う
'''

from decimal import Decimal

df_list2 = []

for df in wbs_df_list:
    df['売上'] = df['売上'].apply(lambda x: Decimal(x.replace(',','')))
    df['売上'] = df['売上'].astype(float)
    df_list2.append(df)
