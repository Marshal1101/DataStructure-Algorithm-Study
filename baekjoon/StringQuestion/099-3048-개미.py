import sys
from collections import deque


def main():
    input = sys.stdin.readline
    N1, N2 = map(int, input().split())
    arr1 = deque(list(input().rstrip()))
    arr1.reverse()
    arr2 = deque(list(input().rstrip()))
    T = int(input())

    i = 0
    tmp1 = deque()
    tmp2 = deque()
    while i < T:
        if arr1:
            tmp1.appendleft(arr1.pop())
        else:
            tmp1.appendleft("")
        if arr2:
            tmp2.append(arr2.popleft())
        else:
            tmp2.append("")
        i += 1
    
    # print(f"tmp1: {tmp1}")
    # print(f"tmp2: {tmp2}")

    i = 0
    while tmp1 or tmp2:
        if tmp1:
            arr2.appendleft(tmp1.pop())
        if tmp2:
            arr2.appendleft(tmp2.pop())
        # if tmp2:
        #     arr1.append(tmp2.popleft())
        # if tmp1:
        #     arr1.append(tmp1.popleft())

    # print(f"arr1:{arr1}")
    # print(f"arr2:{arr2}")

    arr1.extend(arr2)
    # print(f"ans:{arr1}")
    print("".join(arr1))


if __name__ == '__main__':
    main()
