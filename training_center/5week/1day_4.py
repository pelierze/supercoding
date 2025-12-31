"""
# Merge 연습문제
df3 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
df4 = pd.DataFrame({'key': ['B', 'C', 'D'], 'value2': [4, 5, 6]})

# 문제 4: df3과 df4를 'key' 열을 기준으로 outer join 하세요.
"""
import sys
import pandas as pd

def solve(data : str) -> str :
    df3 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
    df4 = pd.DataFrame({'key': ['B', 'C', 'D'], 'value2': [4, 5, 6]})

    result = pd.merge(df3, df4, how = "outer", on = "key")

    return result.to_string()
    

def main() :
    data = sys.stdin.read().strip()
    print(solve(data))

if __name__ == "__main__" :
    main()