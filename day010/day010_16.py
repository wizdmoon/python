import numpy as np

np.random.seed(42)
arr1 = np.random.randint(0, 16, (4, 4))
print('시드 42로 생성한 배열: ')
print(arr1)

np.random.seed(42)
arr2 = np.random.randint(0, 16, (4, 4))
print('\n다시 시드 42로 생성한 배열: ')
print(arr2)