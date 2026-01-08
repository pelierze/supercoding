"""
문제
제1회 피갤컵이 2024년 8월에 열렸다.

제2회 피갤컵은 2025년 3월에 열린다.

이를 통해 피갤컵은 7개월 주기로 열린다는 사실을 알 수 있다.

그렇다면 
$N$번째 피갤컵은 언제 열릴까?

입력
첫째 줄에 정수 
$N$이 주어진다. 
$(1 \le N \le 5)$ 

출력
첫째 줄에 
$N$번째 피갤컵이 열리는 연도와 월을 공백을 두고 출력한다.
"""
import sys

def solve(data: str) -> str:
    N = int(data.strip())

    start_year = 2024   
    start_month_index = 7  

    offset = (N - 1) * 7
    total_month = start_month_index + offset

    year = start_year + (total_month // 12)
    month = (total_month % 12) + 1

    return f"{year} {month}"

def main():
    data = sys.stdin.read().strip()
    print(solve(data))

if __name__ == "__main__":
    main()
