"""
# Sample DataFrame (replace with your actual data)
data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C', 'B'],
        'Value': [10, 20, 15, 25, 18, 12, 22, 28, 19],
        'Group': [1, 2, 1, 2, 1, 2, 1, 2, 1]}
df = pd.DataFrame(data)

# 문제 5: 'Category' 열을 기준으로 그룹화하여 각 그룹의
# 첫 번째 행을 출력하세요.
"""

import sys
import pandas as pd

def solve(data : str) -> str :
    
    data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C', 'B'],
        'Value': [10, 20, 15, 25, 18, 12, 22, 28, 19],
        'Group': [1, 2, 1, 2, 1, 2, 1, 2, 1]}
    
    df = pd.DataFrame(data)
    result = df.groupby("Category").first()

    return result.to_string()

def main() :
    data = sys.stdin.read().strip()

if __name__ == "__main__" :
    main()