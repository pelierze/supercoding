"""
문제
제연이는 그의 생일(2000년 3월 3일)을 기념해 자신이 가장 좋아하는 수를 20000303으로 나눈 나머지를 구해 그 수만큼 잠을 자기로 했다. 제연이가 얼마나 잠을 잘 수 있을지 구하자.

입력
첫째 줄에 제연이가 가장 좋아하는 수 N이 주어진다. (N ≤ 101,000,000)

출력
N을 20000303으로 나눈 나머지를 출력한다.
"""
import sys

def solve(data : str) -> int :
    N = int(data)

    birth = 20000303

    sleep = N % birth

    return sleep

def main() :
    data = sys.stdin.read().strip()

    print(solve(data))


if __name__ == "__main__" :
    main()