from sqlalchemy import create_engine
from sqlalchemy import engine
from sqlalchemy import MetaData
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy import Table, Column, true, false
from sqlalchemy.orm import declarative_base

Base = declarative_base()
# class User(Base):

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

engine = create_engine("sqlite:///EdgeSealInspection.db")
meta_data_obj = MetaData()
user = Table('user', meta_data_obj,
Column('user_id', Integer, primary_key=True),
Column('user_name', String(16), nullable=false),
Column('email_address', String(60)),
Column('nick_name', String(50), nullable=false))
user.create(engine)

engine = create_engine('sqlite:///EdgeSealInspection.db')

meta_data_obj = MetaData()
employees = Table('employees', meta_data_obj,
Column('employee_id', Integer, primary_key=True, key='Employee_ID'),
Column('employee_name', String(60), nullable=false, key='Employee_Name'),
Column('employee_dept', Integer, key='Employee_Department'))

employees.create(engine, checkfirst=true)
print(employees.columns.Employee_Name.type)

# employees.create(engine, checkfirst=True)
# employees.drop(engine, checkfirst=True)


# bật cái checkfirst lên là true để check xem bản tồn tại hay chưa
# để raise alarm nếu bảng có rồi mà còn tạo thêm bảng nữa
# schema.table là lớp table, key để dùng nhận dạng cột thông qua lớp table

# engine.execute('CREATE TABLE Demo (Giang TEXT, Dung TEXT, Nhu INTEGER, Duyen INTEGER)')
# engine.execute("INSERT INTO Demo VALUES ('24', '21', '32', '12')")
# result = engine.execute('SELECT * FROM Demo')
# print(result.fetchall())

# git commit --amend -m "Create Data Frame With Missing Value " // Change Name Of Commit
# threshold is require how many non na value kept
# sqlite cũng giống như sqlite3 nhưng sqlite3 thì nâng cấp hơn
'''