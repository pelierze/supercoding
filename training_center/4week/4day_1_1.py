"""
# 문제 1: titanic.csv 파일을 읽어와서 'PassengerId'를 인덱스로 설정하고,
# 처음 5개의 행을 출력하세요.
"""
import sys
import pandas as pd

def solve (data : str ) -> str :
    df = pd.read_csv("titanic.csv")
    df = df.set_index("PassengerId")

    return df.head(5).to_string()


def main() :
    data = sys.stdin.read().strip()
    print(solve(data))

if __name__ == "__main__" :
    main()
