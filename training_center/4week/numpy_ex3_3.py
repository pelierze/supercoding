# 3. 다음 ndarray를 1차원으로 flatten 하세요.

import numpy as np

data = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

modified_data = data.flatten()

print(modified_data)