def extract_data(df, col1, value1, col2, value2):
    # 値の変数は先頭に@を付け、列名の変数はformat記法を使用
    df_check = df.query("{} == @value1".format(col1)).query("{} == @value2".format(col2)).reset_index(drop=True)
    
    return df_check

if __name__ == '__main__':
    extract_data(df, 'col1', 'val1', 'col2', 'val2')
