def main():
    N = int(input())
    K = int(input())
    if K >= N:
        print(0)
        return
    arr = sorted(list(map(int, input().split())))
    dist = []
    for i in range(N-1):
        dist.append(abs(arr[i] - arr[i+1]))
    dist.sort(reverse=True)

    ans = 0
    for i in range(K-1, len(dist)):
        ans += dist[i]

    print(ans)


if __name__ == '__main__':
    main()