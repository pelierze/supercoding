"""
문제
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

출력
입력으로 주어진 숫자 N개의 합을 출력한다.
"""
import sys

def solve(data : str) -> int :
    data_lines = data.splitlines()
    N = int(data_lines[0])

    Number = data_lines[1]

    number_list = list(map(int, Number))

    result = sum(number_list)

    return result

def main() :
    data = sys.stdin.read().strip()
    print(solve(data))

if __name__ == "__main__" :
    main()