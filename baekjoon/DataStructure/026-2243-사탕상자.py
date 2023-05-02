import sys
import math


def find_candy(tree, start, end, node, rank):
    if start == end:
        return start
    mid = (start + end) // 2
    left = tree[node * 2]
    if left >= rank:
        return find_candy(tree, start, mid, node*2, rank)
    else:
        return find_candy(tree, mid+1, end, node*2+1, rank-left)


def update(tree, start, end, node, idx, diff):
    if end < idx or idx < start:
        pass
    
    elif start == end:
        tree[node] += diff

    else:
        mid = (start + end) // 2
        tmp1 = update(tree, start, mid, node * 2, idx, diff)
        tmp2 = update(tree, mid+1, end, node * 2 + 1, idx, diff)
        tree[node] = tmp1 + tmp2
    return tree[node]


def main():
    input = sys.stdin.readline
    N = 10 ** 6 + 1
    T = int(input())
    width = 2 ** (math.ceil(math.log2(N)) + 1)
    tree = [0] * width
    ans = []
    for _ in range(T):
        q, *sel = list(map(int, input().split()))
        if q ==  1:
            candy = find_candy(tree, 1, N, 1, sel[0])
            ans.append(candy)
            update(tree, 1, N, 1, candy, -1)
        else:
            update(tree, 1, N, 1, sel[0], sel[1])
            
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()