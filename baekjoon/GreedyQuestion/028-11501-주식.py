import sys


def stock(N:int, arr:list) -> int:
    ret = 0
    tmp = 0
    var = arr.pop()
    while arr:
        cur = arr.pop()
        if cur > var:
            ret += tmp
            var = cur
            tmp = 0
        elif cur < var:
            tmp += var - cur
    if tmp:
        ret += tmp

    return ret


def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        arr = [*map(int, input().split())]
        print(stock(N, arr))


if __name__ == '__main__':
    main()