"""
# 문제 3: 'titanic.csv' 파일을 읽어와서 'Survived' 열이 1인 승객들의
# 정보만 추출하여 새로운 DataFrame을 만들고, 'titanic_survived.csv' 파일로
# 저장하세요. 인덱스는 저장하지 마세요.
"""
import sys
import pandas as pd

def solve(data : str) -> str :
    df = pd.read_csv("titanic.csv")

    survived_df = df[df["Survived"] == 1]

    survived_df.to_csv("titanic_survived.csv", index = False)

    return "Saved titanic_survived.csv"

def main() :
    data = sys.stdin.read().strip()
    print(solve(data))

if __name__ == "__main__" :
    main()
