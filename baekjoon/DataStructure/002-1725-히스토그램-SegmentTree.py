import math
import sys

sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
histogram = [int(sys.stdin.readline()) for _ in range(N)]
witdh = 2 ** math.ceil(math.log2(len(histogram)))
segment_tree = [0] * 2 * witdh

def init(start, end, node):
    """segment_tree[node]에 histogram의 최소높이값이 들어간다."""
    if start == end:
        segment_tree[node] = start
        return start

    mid = (start + end) // 2
    left = init(start, mid, node * 2)
    right = init(mid + 1, end, node * 2 + 1)

    if histogram[left] < histogram[right]:
        segment_tree[node] = left
    else:
        segment_tree[node] = right

    return segment_tree[node]


def get_idx_minh(start, end, node, left, right):
    """시작과 끝 인덱스 사이의 최소높이인 인덱스를 반환한다."""
    if left > end or right < start:
        return math.inf
    if start >= left and end <= right:
        return segment_tree[node]

    mid = (start + end) // 2
    left_min_index = get_idx_minh(start, mid, node * 2, left, right)
    right_min_index = get_idx_minh(mid + 1, end, node * 2 + 1, left, right)

    if left_min_index == math.inf:
        return right_min_index
    if right_min_index == math.inf:
        return left_min_index

    if histogram[left_min_index] > histogram[right_min_index]:
        return right_min_index
    else:
        return left_min_index


def get_max_square(left, right):
    """최소높이*가로길이와 최소높이 인덱스 기준의 좌우측 분할시 최대넓이를 비교한다."""
    min_index = get_idx_minh(0, N - 1, 1, left, right)
    max_width = (right - left + 1) * histogram[min_index]

    if left < min_index:
        max_width = max(get_max_square(left, min_index - 1), max_width)

    if right > min_index:
        max_width = max(get_max_square(min_index + 1, right), max_width)

    return max_width

init(0, len(histogram) - 1, 1)

print(get_max_square(0, N-1))