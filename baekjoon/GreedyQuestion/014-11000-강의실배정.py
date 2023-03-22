import sys
from heapq import heappop, heappush


def main():
    input = sys.stdin.readline
    N = int(input())
    st = [tuple(map(int, input().split())) for _ in range(N)]
    st.sort()
    # print(st)
    hq = [st[0][1]]
    for i in range(1, N):
        if st[i][0] >= hq[0]:
            heappop(hq)
        heappush(hq, st[i][1])  

    print(len(hq))

if __name__ == '__main__':
    main()