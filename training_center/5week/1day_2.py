"""
# Concat 연습문제
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

# 문제 2: df1과 df2를 가로 방향으로 연결하세요.
"""
import sys
import pandas as pd

def solve(data : str) -> str :
    df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

    result = pd.concat([df1, df2], axis = 1)
    return result.to_string()

def main() :
    data = sys.stdin.read().strip()
    print(solve(data))

if __name__ == "__main__" :
    main()