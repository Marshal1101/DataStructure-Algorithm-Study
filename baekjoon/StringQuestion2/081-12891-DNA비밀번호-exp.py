import sys
from collections import deque


def main() -> None:
    input = sys.stdin.readline

    _, m = map(int, input().split())
    s = input().strip()
    a, c, g, t = map(int, input().split())

    pw: deque[str] = deque(maxlen=m)
    ca = cc = cg = ct = 0
    result = 0
    for b in s:
        pw.append(b)

        if b == "A": ca += 1
        elif b == "C": cc += 1
        elif b == "G": cg += 1
        elif b == "T": ct += 1

        if len(pw) < m:
            continue

        if ca >= a and cc >= c and cg >= g and ct >= t:
            result += 1

        if pw[0] == "A": ca -= 1
        elif pw[0] == "C": cc -= 1
        elif pw[0] == "G": cg -= 1
        elif pw[0] == "T": ct -= 1

    print(result)


if __name__ == "__main__":
    sys.exit(main())  # type: ignore[func-returns-value]
