import numpy as np

arr = np.arange(12)
print('원본 배열:')
print(arr)

reshaped_arr = arr.reshape(3, 4)
print('\nReshaped 배열:')
print(reshaped_arr)

reshaped_arr = arr.reshape(-1)
print('\n1차원 배열로 변경:')
print(reshaped_arr)

