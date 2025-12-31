"""
# Sample DataFrame (replace with your actual data)
data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C', 'B'],
        'Value': [10, 20, 15, 25, 18, 12, 22, 28, 19],
        'Group': [1, 2, 1, 2, 1, 2, 1, 2, 1]}
df = pd.DataFrame(data)

# 문제 6:  'Group' 열을 기준으로 그룹화 한 뒤, 각 그룹에서
# 'Value' 열의 값이 20 이상인 데이터만 추출하세요.
"""
import sys
import pandas as pd

def solve(data : str) -> str :
    data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C', 'B'],
        'Value': [10, 20, 15, 25, 18, 12, 22, 28, 19],
        'Group': [1, 2, 1, 2, 1, 2, 1, 2, 1]}
    df = pd.DataFrame(data)

    result = df[df["Value"] >= 20]
    

    return result.to_string

def main() :
    data = sys.stdin().read.strip()

if __name__ == "__main__" :
    main()