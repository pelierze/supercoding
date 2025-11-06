import numpy as np

# 2. 다음과 같은 ndarray 를 만드세요.
"""
[[[ 0  1  2  3]
  [ 4  5  6  7]]

 [[ 8  9 10 11]
  [12 13 14 15]]

 [[16 17 18 19]
  [20 21 22 23]]]
shape: (3, 2, 4)
size: 24
demention: 3
data type: int32
memery bytes: 96
"""

A = []
n = 24
for i in range (0, n) :
    A.append(i)

print(A)

data2 = np.array(A, dtype=np.int32).reshape(3, 2, 4)

print(data2)
print("shape:", data2.shape)
print("size:", data2.size)
print("demention:", data2.ndim)
print("data type:", data2.dtype)
print("memery bytes:", data2.nbytes) 