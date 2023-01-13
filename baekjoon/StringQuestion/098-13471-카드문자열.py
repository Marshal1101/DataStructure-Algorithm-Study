import sys
from collections import deque

def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        arr = input().split()
        string = deque([arr[0]])
        for i in range(1, N):
            if arr[i] <= string[0]:
                string.appendleft(arr[i])
            else:
                string.append(arr[i])

        print("".join(string))


if __name__ == '__main__':
    main()