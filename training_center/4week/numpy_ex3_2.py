
# 2. 다음 ndarray를 (2, 2, 3) shape으로 reshape 하세요.

import numpy as np

data = np.arange(12)
modified_data = data.reshape(2, 2, 3)

print(modified_data)