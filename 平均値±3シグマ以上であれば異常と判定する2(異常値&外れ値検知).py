def add_range_judge_outlier_col_to_dataframe(df, col, weight):
    '''
    関数内容
    ・平均値と標準偏差を使用して外れ値検出用の範囲の下限値と上限値を追加したデータフレームを作成する関数
    Input
    ・df:データフレーム
    ・col:外れ値判定をしたいカラム
    ・weight:標準偏差にかける重み
    関数使用方法
    　df = add_range_judge_outlier_col_to_dataframe(df, '_正規化_直前四半期差分', 3)
    '''
    
    df['min_diff_mean_and_sd'] = np.mean(df[col],axis=0) - np.std(df[col],ddof=0,axis=0)*weight
    
    df['max_diff_mean_and_sd'] = np.mean(df[col],axis=0) + np.std(df[col],ddof=0,axis=0)*weight
    
    return df

# 平均値と標準偏差を使用して外れ値検出用の範囲の下限値と上限値を追加
df = add_range_judge_outlier_col_to_dataframe(df, '_正規化_直前四半期差分', 3)

# 平均値±3シグマ以上であれば「1」(全体の約99.7%の中に含まれていないので異常値である)、そうでなければ「0」（全体の約99.7%の中に含まれているので異常値ではない)と判定するカラムを追加
df['外れ値判定'] =\
df.apply(lambda x: 1 if (x['_正規化_直前四半期差分'] <= x['min_diff_mean_and_sd']) and (x['_正規化_直前四半期差分'] >= x['max_diff_mean_and_sd']) else 0, axis=1)
