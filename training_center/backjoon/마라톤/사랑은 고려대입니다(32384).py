"""
문제
사랑은 고려대입니다.

입력
첫 번째 줄에 정수 
$N(1\leq N\leq 10)$이 주어진다.

출력
첫 번째 줄에 LoveisKoreaUniversity를 공백으로 구분하여 
$N$번 출력한다.
"""
import sys

def solve(data : str ) -> str :
    N = int(data)

    result = []

    for i in range (N) :
        result.append("LoveisKoreaUniversity")

    return " ".join(result)


def main() :
    data = sys.stdin.read().strip()
    print(solve(data))

if __name__ == "__main__" :
    main()