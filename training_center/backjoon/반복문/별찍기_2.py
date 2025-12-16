"""
문제
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
"""
import sys

def solve (data : str ) -> int :
    number_star = data.splitlines()

    N = int(number_star[0])
    star = []
    for i in range (1, N + 1 ) :
        star.append(("*" * i).rjust(N))

    return "\n".join(star)

def main() :
    data = sys.stdin.read().strip()
    print(solve(data))


if __name__ == "__main__" :
    main()