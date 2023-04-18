import sys
from collections import Counter


def main():
    input = sys.stdin.readline

    n, m = map(int, input().split())
    counter = Counter(word for _ in range(n) if len(word := input().strip()) >= m)
    words = list(counter.keys())
    words.sort()
    words.sort(key=len, reverse=True)
    words.sort(key=counter.get, reverse=True)
    print("\n".join(words))


if __name__ == "__main__":
    sys.exit(main())
