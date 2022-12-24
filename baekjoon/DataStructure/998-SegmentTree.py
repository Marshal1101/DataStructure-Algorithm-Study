import sys, math


def init(start, end, node, tree, arr) -> None:
    if start == end:
        tree[node] = start
        return tree[node]

    mid = (start + end) // 2
    left_idx = init(start, mid, node * 2, tree, arr)
    right_idx = init(mid+1, end, node * 2 + 1, tree, arr)

    if arr[left_idx] < arr[right_idx]:
        tree[node] = left_idx
    else: tree[node] = right_idx

    return tree[node]


def get_idx_minh(left, right, start, end, node, tree, arr) -> int:
    if start > right or end < left:
        return math.inf
    if left < start and end < right:
        return tree[node]

    mid = (start + end) // 2
    left_idx = get_idx_minh(left, right, start, mid, node*2, tree, arr)
    right_idx = get_idx_minh(left, right, mid+1, end, node*2+1, tree, arr)

    if arr[left_idx] < arr[right_idx]:
        minh_idx = left_idx
    else: minh_idx = right_idx

    return minh_idx


def get_max_square(left, right, start, end, node, tree, arr) -> int:
    minh_idx = get_idx_minh(left, right, start, end, node, tree, arr)
    max_square = (right - left + 1) * arr[minh_idx]

    if left < minh_idx:
        max_square = max(max_square, get_max_square(left, minh_idx-1, start, end, node, tree, arr))
    if minh_idx < right:
        max_square = max(max_square, get_max_square(minh_idx+1, right, start, end, node, tree, arr))

    return max_square


N = int(sys.stdin.readline())
histogram = [int(sys.stdin.readline()) for _ in range(N)]
witdh = 2 ** math.ceil(math.log2(len(histogram)))
segment_tree = [0] * 2 * witdh

init(0, len(histogram) - 1, 1, segment_tree, histogram)
print(get_max_square(0, N-1, 0, N-1, 1, segment_tree, histogram))