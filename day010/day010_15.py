import numpy as np

np.random.seed(42)
arr = np.random.randint(0, 16, (4, 4))

print(arr)

arr[arr % 2 == 0] = 0

print(arr)
