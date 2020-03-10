# 予め日付カラムをdatetime64型に変換しておく
import pandas as pd
import datetime

cf_df1718 =\
cf_df[(cf_df['日付']>= datetime.datetime(2017,4,30))&(cf_df['日付']<= datetime.datetime(2018,3,31))]

cf_df1819 =\
cf_df[(cf_df['日付']>= datetime.datetime(2018,4,30))&(cf_df['日付']<= datetime.datetime(2019,3,31))]

cf_df1920 =\
cf_df[(cf_df['日付']>= datetime.datetime(2019,4,30))&(cf_df['日付']<= datetime.datetime(2020,3,31))]

# 確認
display(cf_df1718.shape, cf_df1819.shape, cf_df1920.shape, cf_df1718.shape[0]+cf_df1819.shape[0]+cf_df1920.shape[0])