import numpy as np

arr = np.array([10, 15, 20, 25, 30])

even_arr = arr[arr % 2 == 0]

print(even_arr)

arr[arr % 2 == 0] = 0

print(arr)