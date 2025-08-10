import numpy as np
import time

list_data = list(range(1000000))
start = time.time()
list_result = [x * 2 for x in list_data]
end = time.time()
print('리스트 연산 시간', end - start)

np_data = np.array(list_data)
start = time.time()
np_result = np_data * 2
end = time.time()
print('Numpy 연산 시간', end - start)