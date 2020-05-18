# カラム名に「売上高」「売上原価」が含まれているカラムのみ抽出し、リストに格納する

uriage_col = df.columns[df.columns.str.contains('売上[高|原価]')].tolist()