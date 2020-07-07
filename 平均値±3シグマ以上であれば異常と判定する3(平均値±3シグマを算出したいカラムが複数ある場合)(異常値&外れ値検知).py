def add_range_judge_outlier_col_to_dataframe2(df, col, weight):
    '''
    関数内容
    ・平均値と標準偏差を使用して外れ値検出用の範囲の下限値と上限値を追加したデータフレームを作成する関数
    Input
    ・df:データフレーム
    ・col:外れ値判定をしたいカラム
    ・weight:標準偏差にかける重み
    関数使用方法
　　　 norm_col_list = norm_df.columns[norm_df.columns.str.endswith('_正規化_直前四半期差分')].tolist()
    　 norm_df_list =\
    　[add_range_judge_outlier_col_to_dataframe(norm_df[[col]], col, 1) for col in norm_col_list]
    　 norm_df = pd.concat([norm_df]+norm_df_list, axis=1)
      #カラム名が重複するので重複しているカラム名を削除
      norm_df = norm_df.loc[:,~norm_df.columns.duplicated()]
    '''
    name = str(col)
    
    df[name + '_lower_limit'] = np.mean(df[col],axis=0) - np.std(df[col],ddof=0,axis=0)*weight
    
    df[name + '_upper_limit'] = np.mean(df[col],axis=0) + np.std(df[col],ddof=0,axis=0)*weight
    
    return df

#平均値と標準偏差を使用して外れ値検出用の範囲の下限値と上限値を追加したいカラムを抽出
norm_col_list = norm_df.columns[norm_df.columns.str.endswith('_正規化_直前四半期差分')].tolist()

# 外れ値を判定したいカラムが複数あるためいったんリスト内包表記を使いデータフレームをリストに格納
norm_df_list =[add_range_judge_outlier_col_to_dataframe2(norm_df[[col]], col, 1) for col in norm_col_list]

# 横に連結
norm_df = pd.concat([norm_df]+norm_df_list, axis=1)

#カラム名が重複するので重複しているカラム名を削除
norm_df = norm_df.loc[:,~norm_df.columns.duplicated()]

