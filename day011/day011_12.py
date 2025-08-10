import pandas as pd

data = {'Product':['Laptop', 'Phone', 'Tablet'], 'Price':[1200, 800, 600]}

df = pd.DataFrame(data)

print(df['Price'])

