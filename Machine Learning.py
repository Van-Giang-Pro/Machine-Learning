
from typing import Text
import numpy as np
import pandas as pd
import sqlalchemy as sal
from sqlalchemy import create_engine
import pyodbc
from sqlalchemy import text
from sqlalchemy import select
import sqlite3
from sqlalchemy import engine
from sqlalchemy.engine.base import Connection

'''
d = {'A':[1,2,np.nan], 'B':[5,np.nan,np.nan], 'C':[1,2,3]}
df = pd.DataFrame(d)

print(df)
print(df.dropna())
print(df.dropna(axis=0))
print(df.dropna(axis=0, thresh=2))
print(df.fillna(value='Giang'))
print(df['A'].fillna(value=df['A'].mean()))
print(df['A'].fillna(value=df['A'].sum()))
print('Fill Value Done')
print('Nguyen Van Giang')
print('Dang Hoag Hanh Dung')

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales':[200,120,340,124,243,350]}
df1 = pd.DataFrame(data)
print(df1)
bycomp = df1.groupby('Company')
print(bycomp.mean())
print(bycomp.sum())
print(bycomp.std())
print(bycomp.sum().loc['FB'])
print(df1.groupby('Company').sum().loc['FB'])

engine = sal.create_engine('mssql+pyodbc://DMT2MESSQLODS/ProcessData?driver=ODBC Driver 17 for SQL Server?Trusted_Connection=yes')
conn = engine.connect()
# data = pd.read_sql_query("Select Top (10) * From [ProcessData].[ProcessHistory].[EdgeSealInspectionLongEdge]", conn)
# print(data)
result = engine.execute("Select Top (100) * From [ProcessData].[ProcessHistory].[EdgeSealInspectionLongEdge]\
Where [ReadTime] = '2018-11-23 20:12:22.5866667' And [SideName] = 'SIDE 4'")
print(result)
for row in result:
        print(row)

connection = sqlite3.connect("Demo.db")
print(connection.total_changes)
cursor = connection.cursor()

connection.execute("CREATE TABLE EdgeSealInspection (Plant TEXT, Site TEXT, BeadWidth INTEGER, GlassToBead INTEGER)")
cursor.execute("INSERT INTO EdgeSealInspection VALUES ('DMT', '1', 8.5, 2.5)")
cursor.execute("INSERT INTO EdgeSealInspection VALUES ('DMT', '2', 8.0, 2.5)")
cursor.execute("INSERT INTO EdgeSealInspection VALUES ('DMT', '1', 7.5, 2.1)")
cursor.execute("INSERT INTO EdgeSealInspection VALUES ('DMT', '2', 7.0, 2.0)")
cursor.execute("INSERT INTO EdgeSealInspection VALUES ('DMT', '1', 8.3, 1.75)")
cursor.execute("INSERT INTO EdgeSealInspection VALUES ('DMT', '1', 6.0, 1.25)")
cursor.execute("INSERT INTO EdgeSealInspection VALUES ('DMT', '2', 7.25, 1.55)")
connection.commit() # save changes to local database
connection.close()

for row in cursor.execute('SELECT * FROM EdgeSealInspection'):
        print(row)
print("Print Data Successfully")
for row in cursor.execute('SELECT * FROM EdgeSealInspection LIMIT 1'):
        print(row)
print("Print Data Successfully")

cursor.execute('SELECT * FROM EdgeSealInspection')
print (cursor.fetchall())
'''

engine = create_engine("sqlite:///NguyenVanGiang.db")
# engine.execute('CREATE TABLE Demo (Giang TEXT, Dung TEXT, Nhu INTEGER, Duyen INTEGER)')
# engine.execute("INSERT INTO Demo VALUES ('24', '21', '32', '12')")
result = engine.execute('SELECT * FROM Demo')
print(result.fetchall())

# git commit --amend -m "Create Data Frame With Missing Value " // Change Name Of Commit
# threshold is require how many non na value kept
# sqlite cũng giống như sqlite3 nhưng sqlite3 thì nâng cấp hơn