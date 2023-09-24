import pandas as pd
from sqlalchemy import create_engine, types

class DataProcessor:
    DATA_MAPPING = {
        '会社情報': {
            'columns': ['Column1', 'Column2', 'Column3'],
            'file_name': '会社情報マスタ',
            'dtype_mapping': {'Column1': types.String, 'Column2': types.Float, 'Column3': types.Integer}
        },
        '勘定科目情報': {
            'columns': ['ColumnA', 'ColumnB', 'ColumnC'],
            'file_name': '勘定科目情報マスタ',
            'dtype_mapping': {'ColumnA': types.String, 'ColumnB': types.Date, 'ColumnC': types.Boolean}
        },
        'マッピング': {
            'columns': ['ColumnX', 'ColumnY', 'ColumnZ'],
            'file_name': 'マッピングマスタ',
            'dtype_mapping': {'ColumnX': types.String, 'ColumnY': types.Float, 'ColumnZ': types.Integer}
        }
    }

    def __init__(self, excel_file_path, server, database, username, password):
        self.excel_file_path = excel_file_path
        self.server = server
        self.database = database
        self.username = username
        self.password = password

    def main(self, custom_sheet_info_mapping=None, custom_dtype_mapping=None):
        # カスタム設定が提供された場合に使用するシート情報とデータ型マッピングを作成
        sheet_info_mapping = self.get_custom_sheet_info_mapping(custom_sheet_info_mapping)
        dtype_mapping = self.get_custom_dtype_mapping(custom_dtype_mapping)

        # Excelファイルから指定のシートを取得
        dfs = {sheet_name: self.read_excel_to_dataframe(sheet_name, columns) for sheet_name, columns in sheet_info_mapping.items()}

        # データの統計情報を表示
        self.print_data_stats(dfs)

        # データフレームをCSVファイルとして出力
        self.export_data_to_csv(dfs)

        # SQLAlchemyを使用してSQL Serverにデータをインポート
        self.import_data_to_sql_server(dfs, dtype_mapping)

    def read_excel_to_dataframe(self, sheet_name, columns):
        # Excelファイルから指定されたシートを取得し、指定された列名で読み込む
        df = pd.read_excel(self.excel_file_path, sheet_name=sheet_name, usecols=columns)
        return df

    def print_data_stats(self, dfs):
        # データの統計情報を取得
        for sheet_name, df in dfs.items():
            print(f'【{sheet_name}の統計情報】')
            print('行と列の長さ\n{}'.format(df.shape))
            print('-'*50)
            print('各カラムの欠損値の数\n{}'.format(df.isnull().sum()))
            print('-'*50)
            print('各カラムのデータ型\n{}'.format(df.dtypes))
            print('-'*50)
            display(df.head(), df.tail())
            print('*'*100)
            print('*'*100)

    def export_data_to_csv(self, dfs):
        # データフレームをCSVファイルとして出力
        for sheet_name, df in dfs.items():
            encoding = 'cp932'
            try:
                df.to_csv(f'{sheet_name}.csv', index=False, encoding=encoding, schema='raw')
                print(f'{sheet_name}.csv を {encoding} エンコーディングで出力しました。')
            except UnicodeEncodeError:
                encoding = 'utf-8'
                df.to_csv(f'{sheet_name}.csv', index=False, encoding=encoding, schema='raw')
                print(f'{sheet_name}.csv を {encoding} エンコーディングで出力しました。')

    def import_data_to_sql_server(self, dfs, dtype_mapping):
        # SQLAlchemyを使用してSQL Serverに接続し、データをインポート
        engine = create_engine(f'mssql+pyodbc://{self.username}:{self.password}@{self.server}/{self.database}')
        
        for sheet_name, df in dfs.items():
            # シートごとのデータ型マッピングを取得
            column_dtype_mapping = dtype_mapping.get(sheet_name, {})
            df.to_sql(sheet_name, con=engine, if_exists='replace', index=False, dtype=column_dtype_mapping)
        
        print('データのインポートが完了しました.')

    def get_custom_sheet_info_mapping(self, custom_sheet_info_mapping):
        # カスタムのシート情報を提供された場合、デフォルト値をマージ
        if custom_sheet_info_mapping:
            sheet_info_mapping = {**DataProcessor.DATA_MAPPING, **custom_sheet_info_mapping}
        else:
            sheet_info_mapping = DataProcessor.DATA_MAPPING
        return sheet_info_mapping

    def get_custom_dtype_mapping(self, custom_dtype_mapping):
        # カスタムのデータ型マッピングを提供された場合、デフォルト値をマージ
        if custom_dtype_mapping:
            dtype_mapping = {**DataProcessor.DATA_MAPPING, **custom_dtype_mapping}
        else:
            dtype_mapping = DataProcessor.DATA_MAPPING
        return dtype_mapping

if __name__ == "__main__":
    excel_file_path = 'your_excel_file.xlsx'
    server = 'your_server'
    database = 'your_database'
    username = 'your_username'
    password = 'your_password'

    processor = DataProcessor(excel_file_path, server, database, username, password)

    # シート名と列名、データ型マッピングをカスタマイズして実行
    custom_sheet_info_mapping = {
        '会社情報': ['CustomColumn1', 'CustomColumn2', 'CustomColumn3'],
        '勘定科目情報': ['CustomColumnA', 'CustomColumnB', 'CustomColumnC'],
        'マッピング': ['CustomColumnX', 'CustomColumnY', 'CustomColumnZ']
    }

    custom_dtype_mapping = {
        '会社情報': {'CustomColumn1': types.String, 'CustomColumn2': types.Float, 'CustomColumn3': types.Integer},
        '勘定科目情報': {'CustomColumnA': types.String, 'CustomColumnB': types.Date, 'CustomColumnC': types.Boolean},
        'マッピング': {'CustomColumnX': types.String, 'CustomColumnY': types.Float, 'CustomColumnZ': types.Integer}
    }

    processor.main(custom_sheet_info_mapping, custom_dtype_mapping)