"""
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	249710	168553	148944	67.995%
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.
"""
import sys

def solve(data : str) -> str :
    number_lines = data.splitlines()

    T = int(number_lines[0])
    result = []

    for i in range (1, T + 1) :
        A, B = map(int, number_lines[i].split())
        result.append(f"Case #{i}: {A} + {B} = {A+B}")

    return "\n".join(result)

def main() :
    data = sys.stdin.read().strip()
    print(solve(data))

if __name__ == "__main__" :
    main()