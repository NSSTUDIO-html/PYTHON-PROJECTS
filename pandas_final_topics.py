
# 🐼 Pandas 
import pandas as pd

# Concatenate
df1 = pd.DataFrame({'A': ['A0', 'A1'], 'B': ['B0', 'B1']})
df2 = pd.DataFrame({'A': ['A2', 'A3'], 'B': ['B2', 'B3']})
result = pd.concat([df1, df2])

# Merge
left = pd.DataFrame({'key': ['K0', 'K1'], 'A': ['A0', 'A1']})
right = pd.DataFrame({'key': ['K0', 'K1'], 'B': ['B0', 'B1']})
merged = pd.merge(left, right, on='key')

# Join
df1 = pd.DataFrame({'A': ['A0'], 'B': ['B0']}, index=['K0'])
df2 = pd.DataFrame({'C': ['C0'], 'D': ['D0']}, index=['K0'])
joined = df1.join(df2)


## 9. Grouping and Aggregating (groupby
df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B'],
    'Values': [10, 20, 30, 40]
})
grouped = df.groupby('Category').sum()


## 10. Pivot Tables & Crosstabs

# Pivot table
df = pd.DataFrame({'A': ['foo', 'foo', 'bar'], 'B': ['one', 'two', 'one'], 'C': [1, 3, 2]})
pivot = df.pivot_table(values='C', index='A', columns='B')

# Crosstab
pd.crosstab(index=df['A'], columns=df['B'])


## 11. Date/Time Handling

date_rng = pd.date_range(start='2023-01-01', periods=5, freq='D')
df = pd.DataFrame(date_rng, columns=['date'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['weekday'] = df['date'].dt.day_name()


## 12. Apply, Map, Lambda

df = pd.DataFrame({'A': [1, 2, 3]})
df['squared'] = df['A'].apply(lambda x: x**2)

# Map
s = pd.Series([1, 2, 3])
s.map({1: 'A', 2: 'B'})


## 13. Visualization with Pandas

import matplotlib.pyplot as plt

df = pd.DataFrame({'x': range(10), 'y': range(10)})
df.plot(x='x', y='y', kind='line')
plt.show()

