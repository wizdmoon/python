import pandas as pd

data = {'ID':[1, 2, 3], 'Name':['Alice', 'Bob', 'Charlie'], "Age":[25, 30, 35]}
df = pd.DataFrame(data)

df['Score'] = [90, 85, 95]

print(df)

df = df.drop(1)

print(df)

df.index = ['a', 'b']
print(df)

df = df.reset_index()
print(df)
