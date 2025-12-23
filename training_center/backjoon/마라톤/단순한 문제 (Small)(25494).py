import sys

def solve(data: str) -> str:
    lines = data.splitlines()
    T = int(lines[0])

    out_lines = []

    for i in range(1, T + 1):
        a, b, c = map(int, lines[i].split())
        cnt = 0

        for x in range(1, a + 1):
            for y in range(1, b + 1):
                r = x % y
                for z in range(1, c + 1):
                   
                    if r == (y % z) and r == (z % x):
                        cnt += 1

        out_lines.append(str(cnt))

    return "\n".join(out_lines)

def main():
    data = sys.stdin.read().strip()
    print(solve(data))

if __name__ == "__main__":
    main()
