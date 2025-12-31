"""
# Sample DataFrame for exercises
data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C', 'B', 'A'],
        'Value': [10, 20, 15, 25, 18, 12, 22, 28, 19, 17],
        'Group': [1, 2, 1, 2, 1, 2, 1, 2, 1, 1],
        'Date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05',
                               '2024-01-06', '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10']),
        'Sales': [100, 150, 120, 200, 180, 110, 190, 220, 170, 130]}
df = pd.DataFrame(data)

# 문제 8: 각 'Group'별 'Value'의 평균을 구하고, 'Group'을 기준으로 정렬하세요.
"""
import sys
import pandas as pd


def solve(data : str) -> str :
    data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C', 'B', 'A'],
        'Value': [10, 20, 15, 25, 18, 12, 22, 28, 19, 17],
        'Group': [1, 2, 1, 2, 1, 2, 1, 2, 1, 1],
        'Date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05',
                               '2024-01-06', '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10']),
        'Sales': [100, 150, 120, 200, 180, 110, 190, 220, 170, 130]}
    df = pd.DataFrame(data)

    group_mean = df.groupby("Group")["Value"].mean()
    result = group_mean.sort_index()

    return result.to_string()
    
    

def main() :
    data = sys.stdin.read().strip()
    print(solve(data))

if __name__ == "__main__" :
    main()