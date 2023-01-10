import sys
from collections import deque


def check_ppap(string: str) -> bool:
    stack = deque()
    is_prevA = False
    for i in range(len(string)):
        if string[i] == 'A':
            if is_prevA: return False
            is_prevA = True
        else:
            if not is_prevA: 
                stack.append('P')
            else:
                if len(stack) > 1:
                    stack.pop()
                    is_prevA = False
                else: return False
    
    if is_prevA or len(stack) > 1: return False
    else: return True


def main():
    # if check_ppap(sys.stdin.readline().rstrip()):
    #     print("PPAP")
    # else:
    #     print("NP")
    while (string := sys.stdin.readline().rstrip()) != "":
        if check_ppap(string): print("PPAP")
        else: print("NP")


if __name__ == '__main__':
    main()