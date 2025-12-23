"""
문제
밤고는 
100원 동전을 
N개 갖고 있고, 그 돈으로 가격이 
M원인 초코바를 사 먹으려고 한다. 밤고는 갖고 있는 돈으로 초코바를 사 먹을 수 있는지 알고 싶어 한다.

밤고가 가진 돈이 초코바의 가격 이상이면 밤고는 초코바를 살 수 있다. 밤고가 가진 돈이 초코바를 사기에 충분한지 판단해주자.

입력
첫 번째 줄에 두 정수 
N과 
M이 공백을 사이에 두고 주어진다. (
1 <= N <= 100, 
1 <= M <= 10000)

출력
밤고가 초코바를 살 수 있으면 Yes를, 없으면 No를 출력한다.
"""
import sys

def solve(data : str) -> str :
    lines = data.splitlines()

    N, M = map(int, lines[0].split())

    if (100 * N) >= M :
        return "Yes"
    
    else :
        return "No"


def main() :
    data = sys.stdin.read().strip()
    print(solve(data))

if __name__ == "__main__" :
    main()