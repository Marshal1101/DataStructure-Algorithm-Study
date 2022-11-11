import sys;
from math import ceil, log2
input = sys.stdin.readline


def get_empty_segment_tree(N):
    height = ceil(log2(N))
    size = (1 << (height + 1))
    return [0] * size


def set_init_segment_tree(arr, tree, start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] += set_init_segment_tree(arr, tree, start, mid, 2*node)
    tree[node] += set_init_segment_tree(arr, tree, mid+1, end, 2*node+1)
    return tree[node]


def set_update_tree(arr, tree, index, diff, start, end, node):
    if index < start or index > end: return
    tree[node] += diff
    if start == end: return

    mid = (start + end) // 2
    set_update_tree(arr, tree, index, diff, start, mid, 2*node)
    set_update_tree(arr, tree, index, diff, mid+1, end, 2*node+1)


def get_sum_value(tree, left, right, start, end, node):
    if left > end or right < start: return 0
    if left <= start and end <= right: return tree[node]

    mid = (start + end) // 2
    return (
        get_sum_value(tree, left, right, start, mid, 2*node) +
        get_sum_value(tree, left, right, mid+1, end, 2*node+1)
    )


def main():
    N, Q = map(int, input().split())
    arr = [-1] + list(map(int, input().split()))

    tree = get_empty_segment_tree(N)
    set_init_segment_tree(arr, tree, 1, N, 1)

    for _ in range(Q):
        X, Y, A, B = map(int, input().split())
        left, right = (X, Y) if X <= Y else (Y, X)
        print(get_sum_value(tree, left, right, 1, N, 1))

        diff = B - arr[A]
        arr[A] = B
        set_update_tree(arr, tree, A, diff, 1, N, 1)


if __name__ == '__main__':
    main()