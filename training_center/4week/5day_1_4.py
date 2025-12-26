"""
# Sample DataFrame (replace with your actual data)
data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C', 'B'],
        'Value': [10, 20, 15, 25, 18, 12, 22, 28, 19],
        'Group': [1, 2, 1, 2, 1, 2, 1, 2, 1]}
df = pd.DataFrame(data)

# 문제 4: 'Category' 열을 기준으로 그룹화하여 각 카테고리별
# 'Value' 열의 합계를 구하고, 합계가 30 이상인 그룹만 출력하세요.
"""
import pandas as pd

def solve() :
    data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C', 'B'],
        'Value': [10, 20, 15, 25, 18, 12, 22, 28, 19],
        'Group': [1, 2, 1, 2, 1, 2, 1, 2, 1]}
    df = pd.DataFrame(data)

    group_sum = df.groupby("Category")["Value"].sum()
    filtered = group_sum[group_sum >= 30]

    return filtered.to_string()

def main() :
    print(solve())

if __name__ == "__main__" :
    main()