import sqlalchemy
from sqlalchemy import create_engine
import urllib

dsn = 'Driver={SQL Server Native Client 11.0};Server=xxxx;Database=database100;trusted_connection=Yes'
dsn = urllib.parse.quote_plus(dsn)
engine = sqlalchemy.create_engine(f'mssql+pyodbc:///?odbc_connect={dsn}')
conn = engine.connect()

query='''
SELECT 
      [コード]
      ,[決算月]
FROM
      [dbo].[Table_All]
'''
df = pd.read_sql(query, con=conn)