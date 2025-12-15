"""
문제
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

출력
1부터 n까지 합을 출력한다.
"""
import sys

def solve(data: int) -> int :
    number = int(data)
    result = 0
    for i in range (1, number + 1) :
        result = result + i
    
    return result


def main() :
    data = int(sys.stdin.read().strip())
    
    print(solve(data))

if __name__ == "__main__" :
    main()