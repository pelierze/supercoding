"""
# 문제 2: 'titanic.csv' 파일에서 'Age' 열의 평균값을 계산하세요.

"""
import sys
import pandas as pd

def solve(data : str ) -> str :
    df = pd.read_csv("titanic.csv")
    age_mean = df["Age"].mean()

    return str(age_mean)

    

def main():
    data = sys.stdin.read().strip()
    print(solve(data))

if __name__ == "__main__" :
    main()

