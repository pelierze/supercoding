#[NumPy_인덱싱 & 슬라이싱] 사수 도움 요청 업무①
# Indexing & Slicing 연습문제
import numpy as np

# 문제 1: 다음 ndarray에서 [[11, 12], [16, 17]]을 추출하세요.
a = np.arange(1, 26).reshape(5, 5)
print("Problem 1:\n", a)

indices_a = np.where((a == 11) | (a == 12) | (a == 16) | (a == 17))
rows, cols = indices_a[0], indices_a[1]

result1 = a[rows.min() : rows.max()+1, cols.min() : cols.max()+1]

print("Result 1:\n", result1)

# 문제 2: 다음 ndarray에서 [[2, 3], [6, 7]]을 추출하세요.
b = np.arange(1, 13).reshape(3, 4)
print("\nProblem 2:\n", b)
indices_b = np.where((b == 2) | (b == 3) | (b == 6) | (b ==7))

rows, cols = indices_b[0], indices_b[1]

result2 = b[rows.min() : rows.max()+1, cols.min() : cols.max()+1]

print("Result 2:\n", result2)

# 문제 3: 다음 3차원 ndarray에서 (1,1,1), (1,2,2), (2,0,0) 위치의 요소를 추출하세요.
c = np.arange(1, 28).reshape(3, 3, 3)
print("\nProblem 3:\n", c)
indices_c = ((1, 1, 2), (1, 2, 0), (1, 2, 0)) # Your code here 튜플 형태의 인덱스를 생성
result3 = c[indices_c] # Your code here
print("Result 3:\n", result3)

# 문제 4: 다음 ndarray에서 홀수 번째 행과 열만 추출하세요.
d = np.arange(1, 26).reshape(5, 5)
print("\nProblem 4:\n", d)

result4 = d[::2, ::2]

print("Result 4:\n", result4)

# 문제 5: 4차원 ndarray에서 특정 부분을 추출하는 연습
e = np.arange(1, 121).reshape(2, 3, 4, 5)

# 다음 요소들을 추출하는 코드 작성
# 1. 10번째 숫자
# 2. 17번째 숫자
# 3. 76번째 숫자
# 4. 43번째 숫자
# 5. 66번째 숫자

print("\nProblem 5:\n", e.shape)
print("Problem 5:", e)

result5_1 = e.flat[9]   # 10번째 (index 9)
result5_2 = e.flat[16]  # 17번째 (index 16)
result5_3 = e.flat[75]  # 76번째 (index 75)
result5_4 = e.flat[42]  # 43번째 (index 42)
result5_5 = e.flat[65]  # 66번째 (index 65)

print("Result 5_1:", result5_1)
print("Result 5_2:", result5_2)
print("Result 5_3:", result5_3)
print("Result 5_4:", result5_4)
print("Result 5_5:", result5_5)