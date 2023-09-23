import sys


def main():
    input = sys.stdin.readline
    w = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
    A = input().rstrip()
    B = input().rstrip()
    wlist = []
    for i in range(len(A)):
        wlist.append(w[ord(A[i]) - 65])
        wlist.append(w[ord(B[i]) - 65])

    while len(wlist) > 2:
        n_wlist = []
        for i in range(1, len(wlist)):
            n_wlist.append(((wlist[i-1] + wlist[i]) % 10))
        wlist = n_wlist

    print(*wlist, sep="")


if __name__ == '__main__':
    main()