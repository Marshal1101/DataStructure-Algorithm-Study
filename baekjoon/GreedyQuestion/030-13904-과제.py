import sys, heapq as hq


def main():
    input = sys.stdin.readline
    N = int(input())
    sub = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x:(x[0], -x[1]))
    heap = [sub[0][1]]
    time = 1
    for i in range(1, N):
        t, point = sub[i]
        if time < t:
            hq.heappush(heap, point)
            time += 1
        else:
            if point > heap[0]:
                hq.heappop(heap)
                hq.heappush(heap, point)

    print(sum(heap))


if __name__ == '__main__':
    main()
