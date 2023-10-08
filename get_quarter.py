import datetime

import pandas as pd

def get_quarter(closing_date, max_date):
    ''''決算日と最新日付の値から最新日付時の四半期を取得する'''
    
    # 引数で与えられたそれぞれの日付を日付型に変換
    datetype_closing_date = pd.to_datetime(closing_date)
    datetype_max_date = pd.to_datetime(max_date)
    # 決算月
    int_closing_month = datetype_closing_date.month
    # 最新日付における決算月
    int_max_month = datetype_max_date.month
    
    month_mod = ((int_max_month - 1) + (12- int_closing_month)) % 12
    
    quater = month_mod // 3 + 1
    
    output_quarter = f'{quater}Q'
    
    return output_quarter


if __name__ == '__main__':
    closing_date= '2024/3/31'
    max_date_list = ['2023/6/30', '2023/9/30', '2023/12/31', '2024/3/31']
    
    print(f'決算日:{closing_date}')
    for max_date in max_date_list:
        print(f'最新日付:{max_date}', f'四半期:{get_quarter(closing_date, max_date)}')
    
    print()
    closing_date= '2023/9/30'
    print(f'決算日:{closing_date}')
    for max_date in max_date_list:
        print(f'最新日付:{max_date}', f'四半期:{get_quarter(closing_date, max_date)}')


    
    
    
    
    

