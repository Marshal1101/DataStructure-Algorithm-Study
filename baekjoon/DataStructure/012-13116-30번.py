import sys

def LCA(n1, n2):
    while n1 != n2:
        if n1 < n2:
            n2 = (n2 - 2) // 2 + 1
        else:
            n1 = (n1 - 2) // 2 + 1
    return n1


def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n1, n2 = map(int, input().split())
        print(10 * LCA(n1, n2))


if __name__ == '__main__':
    main()