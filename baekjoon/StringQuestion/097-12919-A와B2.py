import sys
from collections import deque


def func_ab(S: list, T: deque, ptr: int) -> bool:

    if len(S) == len(T):
        if S == T: return True
        else: return False

    if ptr == 0 and T[0] == "B":
        T.pop(0)
        T.reverse()
    elif ptr == -1 and T[-1] == "A":
        T.pop()
    else: return False

    ans1 = func_ab(S, T[:], 0)
    ans2 = func_ab(S, T[:], -1)
    return ans1 | ans2


def main():
    input = sys.stdin.readline
    S = list(input().rstrip())
    T = list(input().rstrip())
    
    if (func_ab(S, T[:], 0) or func_ab(S, T[:], -1)):
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()