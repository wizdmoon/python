import pandas as pd

data = {'Apple':3, 'Banana':5, 'Cherry':2}

s = pd.Series(data)
print(s)
print(s['Apple'])
print(s[['Apple', 'Cherry']])

print(s[s > 3])