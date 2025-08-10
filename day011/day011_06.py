import pandas as pd

data = {'ID':[1, 2, 3], 'Name':['Alice', 'Bob', 'Charlie'], "Age":[25, 30, 35]}
df = pd.DataFrame(data, index=[1,2,3])

print(df)
# print(df["Name"])
print(df.iloc[1])
print(df.loc[1])