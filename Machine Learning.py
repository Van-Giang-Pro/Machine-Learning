import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan], 'B':[5,np.nan,np.nan], 'C':[1,2,3]}
df = pd.DataFrame(d)
'''
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
'''

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











# git commit --amend -m "Create Data Frame With Missing Value " // Change Name Of Commit
# threshold is require how many non na value kept