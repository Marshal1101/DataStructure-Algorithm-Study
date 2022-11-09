import sys
from math import ceil, log2
input = sys.stdin.readline


def get_init_segment_tree(N):
    tree_height = ceil(log2(N))
    tree_size = (1 << (tree_height + 1))
    return [0] * tree_size


def find(tree, left, right, start, end, node):
    if start > right or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    return find(tree,left,right,start,mid,node*2) + find(tree,left,right,mid+1,end,node*2+1)


def update(tree, val, diff, start, end, node):
    if start == end:
        tree[node] += diff
        return
    
    mid = (start + end) // 2
    if val <= mid: update(tree, val, diff, start, mid, node * 2)
    else: update(tree, val, diff, mid+1, end, node * 2 + 1)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def main():
    N = int(input())
    data = list(map(int, input().split()))
    tree = get_init_segment_tree(N)
    ans = 0
    for i in data:
        # print(find(tree, i+1, size, 1, size, 1))
        ans += (i - 1) - find(tree, 1, i-1, 1, N, 1)
        update(tree, i, 1, 1, N, 1)

    print(ans)


if __name__ == '__main__':
    main()