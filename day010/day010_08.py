import numpy as np
import sys

list_data = list(range(1000))
np_data = np.array(list_data)

print('리스트 크기: ', sys.getsizeof(list_data), 'bytes')
print('넘파이 크기: ', np_data.nbytes, 'bytes')