"""
문제
N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.

출력
출력형식과 같게 N*1부터 N*9까지 출력한다.
"""


import sys

def solve(data: str) -> str:
    n = int(data)
    lines = []

    for i in range (1, 10) :
        lines.append(f"{n} * {i} = {n * i}")
    
    return "\n".join(lines)

def main():
    data = sys.stdin.read().strip()
    print(solve(data))

if __name__ == "__main__":
    main()
