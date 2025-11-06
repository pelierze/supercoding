# 4. 다음 ndarray를 reshape하여 shape이 (3, -1)이 되도록 하세요. (-1은 자동 계산)

import numpy as np

data = np.arange(18)

modified_data = data.reshape(3, -1)

print(modified_data)