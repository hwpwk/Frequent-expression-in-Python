def loop_xlsx_to_csv(file_name_list, df_list, processed_data_path=r'C:/Users/data/', encoding='cp932'):
    '''
    関数内容
    ・xlsxファイルをcsvファイルに変換する関数
    Input
    ・file_name_list：出力するファイル名に名付ける名称を格納したリスト
    ・df_list：出力するデータフレームを格納したリスト
    ・processed_data_path：csv変換後のデータを格納したいディレクトリ
    関数使用方法
    # 受領データを加工後したファイルを格納するディレクトリ
    out_path = r'C:/Users/data/'
    # 実行
    loop_xlsx_to_csv(file_raw_name_list, final_bspl_df_list, out_path)
    '''

    for file_name, df in zip(file_name_list, df_list):
        df.to_csv(processed_data_path + file_name + '.csv', index=False, encoding=encoding)
        print(file_name + 'のcsvファイルへの変換が完了しました。')
    
    print('csvファイルへの変換が完了しました。')