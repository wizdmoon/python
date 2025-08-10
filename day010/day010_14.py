import numpy as np

arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

row_sum = np.sum(arr, axis=1)

col_sum = np.sum(arr, axis=0)

print('각 행의 합:', row_sum)
print('각 열의 합:', col_sum)