import sys


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a == b:
        return False
    if a < b: parent[b] = a
    else: parent[a] = b
    return True

def main():
    input = sys.stdin.readline
    N = int(input())
    M = int(input())
    edges = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))
    edges.sort()

    total = 0
    parent = [i for i in range(N+1)]
    for i in range(M):
        c, a, b = edges[i]
        if union(parent, a, b):
            total += c
    print(total)


if __name__ == '__main__':
    main()