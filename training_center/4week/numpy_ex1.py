# 1. 다음 ndarray의 shape, size, dimention, data type, 그리고 메모리 사용량을 출력 하세요
import numpy as np

data1 = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, -11, 12.2], [12, 14, 15, 16, 17, "18"]], float)

print(data1)
print("shape:", data1.shape)
print("size:", data1.size)
print("dimention:", data1.ndim)
print("data type:", data1.dtype)
print("memery bytes:", data1.nbytes)