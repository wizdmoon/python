import pandas as pd

dates = pd.date_range('2024-01-01', periods=4)
s = pd.Series([100, 200, 300, 400], index=dates)

print(s)