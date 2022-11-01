import sys, math

MAX =  10 ** 9 + 1
MIN = 0

def init_tree(arr, tree, start, end, node = 1):
    if start == end:
        tree[node] = arr[start]
        return tree[node]

    mid = (start + end) // 2
    left_val = init_tree(arr, tree, start, mid, node * 2)
    right_val = init_tree(arr, tree, mid+1, end, node * 2 + 1)
    min_val = left_val if left_val < right_val else right_val
    tree[node] = min_val
    return tree[node]


def get_val(tree, left, right, start, end, node):
    if right < start or left > end:
        return MAX
    if left <= start and right >= end:
        return tree[node]

    mid = (start + end) // 2
    left_val = get_val(tree, left, right, start, mid, node * 2)
    right_val = get_val(tree, left, right, mid+1, end, node * 2 + 1)
    min_val = left_val if left_val < right_val else right_val
    return min_val


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = [0] + [int(input()) for _ in range(N)]
    width = 2 ** math.ceil(math.log2(len(arr)))
    tree = [MAX for _ in range(2 * width)]

    init_tree(arr, tree, 1, N, 1)
    
    for _ in range(M):
        start, end = map(int, input().split())
        print(get_val(tree, start, end, 1, N, 1))


if __name__ == '__main__':
    main()