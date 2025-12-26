"""
# 문제 5: 'titanic.csv' 파일에서 'Pclass'가 1 또는 2인 승객들의 'Name'과
# 'Age' 정보를 새로운 DataFrame으로 만들고 'titanic_highclass.xlsx'
# 파일의 'highclass' 시트에 저장하세요. 인덱스는 저장하지 마세요.
"""
import sys
import pandas as pd

def solve() :
    df = pd.read_csv("titanic.csv")

def main():
    data = sys.stdin.read().strip()
    print(solve(data))

if __name__ == "__main__" :
    main()
"""
import sys
import pandas as pd

def solve(data : str) -> str :
    df = pd.read_csv("titanic.csv")
    df_filtered = df[(df["Pclass"] == 1) | (df["Pclass"] == 2)]
    df_result = df_filtered[["Name", "Age"]]

    df_result.to_excel(
        "titanic_highclass.xlsx",
        sheet_name = "hightclass",
        index = False
    )

    return "Saved titanic_highclass.xlsx"



def main():
    data = sys.stdin.read().strip()
    print(solve(data))

if __name__ == "__main__" :
    main()
"""