"""
# Sample DataFrame (replace with your actual data)
data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C', 'B'],
        'Value': [10, 20, 15, 25, 18, 12, 22, 28, 19],
        'Group': [1, 2, 1, 2, 1, 2, 1, 2, 1]}
df = pd.DataFrame(data)

# 문제 3: 'Category' 와 'Group' 열을 기준으로 그룹화하여 각
# 그룹별 데이터의 개수를 구하세요.
"""
import pandas as pd

def solve() :
    data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C', 'B'],
        'Value': [10, 20, 15, 25, 18, 12, 22, 28, 19],
        'Group': [1, 2, 1, 2, 1, 2, 1, 2, 1]}
    df = pd.DataFrame(data)

    result = df.groupby(["Category", "Group"]).size()

    return result.to_string()


def main():
    print(solve())

if __name__ == "__main__" :
    main()