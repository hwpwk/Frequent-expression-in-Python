import glob
import subprocess


SERVER_NAME = r'OWNER-PC\SQLEXPRESS' # SELECT @@SERVERNAMEで表示される値
DATABASE_NAME = 'FeeForUsingCreditCard2'
# SQLファイルのリストを取得し、ソートする
sql_path_list = sorted(glob.glob(r'C:\Users\Owner\Documents\SQL Server Management Studio\test\*.sql'))

# バッチファイルのコマンドをPythonのリストとして定義
batch_commands = [
    'echo off'
]

for sql_file in sql_path_list:
    batch_commands.append(f'echo Executing {sql_file} >> execution_log.txt')
    batch_commands.append(f'sqlcmd -S {SERVER_NAME} -d {DATABASE_NAME} -E -i "{sql_file}" -o "output.log"')  # SQLの出力を別のファイルに保存
    batch_commands.append(f'echo Execution of {sql_file} completed. >> execution_log.txt')

# バッチファイル内の各コマンドを順番に実行
for cmd in batch_commands:
    subprocess.run(cmd, shell=True)

print("Batch file executed successfully.")
