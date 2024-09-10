import pandas as pd
s=pd.Series([10,20,30,40],index=['a','b','c','d'])
print(s)
print(s['a'])
data ={
    'name':['john','anna','peter'],
    'age':[28,24,35],
    'city':['newyork','paris','berlin']
}
df=pd.DataFrame(data)
print(df)

df = pd.read_csv('data.csv')
print(df.head())
#prints the top 5 rows of a data frame

print(df['Name'])
print(df[['Name','Age']])

# Accessing by index (row 0)
print(df.loc[0])

# Accessing by position (row 0)
print(df.iloc[0])

# Slicing rows (rows 0 to 1)
print(df[0:2])

print('=====')
filteredDf = df[df['Age']>40]
print(filteredDf)

print(filteredDf.describe())

df['age next year'] = df['Age']+1
print(df)

df.fillna(0,inplace=True)
print(df)

df.to_csv('updatedData.csv',index=True, index_label = 'index')