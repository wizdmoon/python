# 데이터프레임의 인덱스 리셋
import pandas as pd
data = {'ID' :[1,2,3,], 'Name': ['Alice', 'Bob', "Charlie"], 'Age':[25,30,35] }
df1 = pd.DataFrame(data)
print(df1)
print("="*50)
df1 = df1.drop(1)  
print(df1)
print("="*50)
df1.index = ['a','b']
print(df1)
print("="*50)
df1 = df1.reset_index()
print(df1)