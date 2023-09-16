import datetime
import pandas as pd
import numpy as np
from IPython.core.display import display
from functools import wraps


def display_df_shape_and_header(df, top_num=1):
    '''データフレームの行列数と先頭top_num行を表示する関数'''
    display(df.shape, df.head(top_num))

def measure_time(func):
    '''処理時間を測定する関数'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 処理の開始時刻を記録
        start_time = datetime.datetime.now()
        print(f'{start_time}に処理を開始しました。')
        # 関数を実行
        result = func( *args, **kwargs)
        # 処理の終了時刻を記録
        end_time = datetime.datetime.now()
        print(f'{end_time}に処理を終了しました。')
        # 処理時間を計算
        elapsed_time = end_time - start_time
        # 処理時間を秒、分、時間単位で表示
        seconds = elapsed_time.total_seconds()
        minutes = seconds / 60
        hours = minutes / 60
        print(f'処理時間: {seconds} 秒')
        print(f'処理時間: {minutes} 分')
        print(f'処理時間: {hours} 時間')

        return result

    return wrapper


