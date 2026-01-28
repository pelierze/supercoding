"""
문제
단어 
$S$와 정수 
$i$가 주어졌을 때, 
$S$의 
$i$번째 글자를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 영어 소문자와 대문자로만 이루어진 단어 
$S$가 주어진다. 단어의 길이는 최대 
$1\,000$이다.

둘째 줄에 정수 
$i$가 주어진다. (
$1 \le i \le \left|S\right|$)

출력
 
$S$의 
$i$번째 글자를 출력한다.
"""
import sys

def solve(data : str) -> str :
    data_lines = data.splitlines()
    i = int(data_lines[1])

    S = data_lines[0]

    result = S[i-1]
    
    return result

def main() :
    data = sys.stdin.read().strip()
    print(solve(data))

if __name__ == "__main__" :
    main()