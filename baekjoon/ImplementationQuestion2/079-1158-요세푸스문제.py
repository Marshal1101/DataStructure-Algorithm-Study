from collections import deque


def main():
    N, K = map(int, input().split())
    queue = deque([i for i in range(1, N+1)])
    ans = []
    while queue:
        s = 0
        while s < K-1:
            num = queue.popleft()
            queue.append(num)
            s += 1
        num = queue.popleft()
        ans.append(num)

    print("<", end="")
    print(*ans, sep=", ", end="")
    print(">")

if __name__ == '__main__':
    main()