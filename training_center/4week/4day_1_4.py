"""
# 문제 4: 'titanic.xlsx' 파일의 'passengers' 시트에서 'Fare' 열의
# 최댓값과 최솟값을 출력하세요. 'PassengerId' 열을 인덱스로 사용하세요.
"""
import sys
import pandas as pd

def solve(data: str) -> str :
    df = pd.read_excel("titanic.xlsx", sheet_name = "passengers")
    df = df.set_index("PassengerId")

    Fare_max = df["Fare"].max()
    Fare_min = df["Fare"].min()

    return f"{Fare_max}\n{Fare_min}"

def main() :
    data = sys.stdin.read().strip()
    print(solve(data))

if __name__ == "__main__" :
    main()
