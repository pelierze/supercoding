"""
x + y + 3z = 4
x + 2y - z - 2
2x + 3y + 2z = 6

numpy를 이용하여 위의 행렬 연산으로 연립방정식을 풀어 보세요
"""

import numpy as np

A = np.array([
    [1, 1, 3],
    [1, 2, -1],
    [2, 3, 2]
])
B = np.array([4, 2, 6])

A_ = np.linalg.pinv(A)
print(A_)

x = A_ @ B
print(x)

print(A @ x)
