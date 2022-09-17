import sys


def hanoii(n, start, end) :
    if n == 1 :
        return str(start) + " " + str(end) + "\n"

    mid = 6 - start - end
    return hanoii(n-1, start, mid) + hanoii(1, start, end) + hanoii(n-1, mid, end)

def main() :
    N = int(sys.stdin.readline())
    print(2**N-1)
    print(hanoii(N, 1, 3))


if __name__ == '__main__':
    main()