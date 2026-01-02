"""
# Sample DataFrame for exercises
data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C', 'B', 'A'],
        'Value': [10, 20, 15, 25, 18, 12, 22, 28, 19, 17],
        'Group': [1, 2, 1, 2, 1, 2, 1, 2, 1, 1],
        'Date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05',
                               '2024-01-06', '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10']),
        'Sales': [100, 150, 120, 200, 180, 110, 190, 220, 170, 130]}
df = pd.DataFrame(data)

# 문제 16: 'Category'열을 기준으로 데이터를 그룹화하고 각 그룹의
# 'Value' 열의 표준편차를 구하세요.
"""
import sys
import pandas as pd


def solve(data) :
    data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C', 'B', 'A'],
        'Value': [10, 20, 15, 25, 18, 12, 22, 28, 19, 17],
        'Group': [1, 2, 1, 2, 1, 2, 1, 2, 1, 1],
        'Date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05',
                               '2024-01-06', '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10']),
        'Sales': [100, 150, 120, 200, 180, 110, 190, 220, 170, 130]}
    df = pd.DataFrame(data)

    df = df.groupby("Category")["Value"].std()

    return df
    

def main() :
    data = sys.stdin.read().strip()
    print(solve(data))

if __name__ == "__main__" :
    main()