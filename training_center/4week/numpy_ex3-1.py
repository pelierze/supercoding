
# #### reshape 연습문제

# 1. 다음 ndarray를 (2, 6) shape으로 reshape 하세요.

import numpy as np

data1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
modified_data = data1.reshape(2, 6)

print(modified_data)