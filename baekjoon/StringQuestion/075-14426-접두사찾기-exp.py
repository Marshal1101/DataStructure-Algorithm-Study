import sys
from bisect import bisect_left


def main() -> None:
    input = sys.stdin.readline

    n, m = map(int, input().split())
    arr = sorted(input().rstrip() for _ in range(n))
    print(sum((i := bisect_left(arr, p := input().rstrip())) < n and arr[i].startswith(p) for _ in range(m)))


if __name__ == "__main__":
    sys.exit(main())
