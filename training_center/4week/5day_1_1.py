"""
# Sample DataFrame (replace with your actual data)
data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C', 'B'],
        'Value': [10, 20, 15, 25, 18, 12, 22, 28, 19],
        'Group': [1, 2, 1, 2, 1, 2, 1, 2, 1]}
df = pd.DataFrame(data)

# 문제 1: 'Category' 열을 기준으로 그룹화하여 각 카테고리별
# 'Value' 열의 평균을 구하세요.
"""
import pandas as pd

def solve() -> str :
    data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C', 'B'],
        'Value': [10, 20, 15, 25, 18, 12, 22, 28, 19],
        'Group': [1, 2, 1, 2, 1, 2, 1, 2, 1]}
    df = pd.DataFrame(data)
    
    result = df.groupby("Category")["Value"].mean

    return result.to_string()

def main() :
    print(solve())

if __name__ == "__main__" : 
    main()