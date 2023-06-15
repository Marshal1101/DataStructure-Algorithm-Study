import sys
from collections import Counter

def main():
    input = sys.stdin.readline
    M = int(input())
    string = input().rstrip()
    m = M
    min_changed = len(string)
    while m > 0:
        changed = 0
        for l in range(m):
            sub = string[l:len(string):m]
            most_count = Counter(sub).most_common(1)
            changed += len(sub) - most_count[0][1]
        if min_changed > changed:
            min_changed = changed
        if min_changed == 0:
            break
        m -= 1

    print(min_changed)


if __name__ == '__main__':
    main()