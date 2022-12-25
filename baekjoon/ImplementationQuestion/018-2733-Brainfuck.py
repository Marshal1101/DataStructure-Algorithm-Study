import sys
from collections import defaultdict

def compile_BF(code: str):
    ret = ""
    arr = [0] * 32768
    ptr = 0

    # 1st
    stack = []
    goto = defaultdict(int)
    is_error = False
    for i in range(len(code)):
        if code[i] == "[":
            stack.append(i)

        elif code[i] == "]":
            if len(stack) != 0:
                dest = stack.pop()
                goto[i] = dest
                goto[dest] = i
            else:
                is_error = True
                break

    if is_error or len(stack) > 0: return "COMPILE ERROR"

    # 2nd
    i = 0
    while i < len(code):
        if code[i] == ">":
            if ptr != 32767:
                ptr += 1
            else: ptr = 0

        elif code[i] == "<":
            if ptr != 0:
                ptr -= 1
            else: ptr = 32767

        elif code[i] == "+":
            if arr[ptr] != 255:
                arr[ptr] += 1
            else: arr[ptr] = 0

        elif code[i] == "-":
            if arr[ptr] != 0:
                arr[ptr] -= 1
            else: arr[ptr] = 255

        elif code[i] == ".":
            ret += chr(arr[ptr])

        elif code[i] == "[":
            if arr[ptr] == 0:
                i = goto[i]

        elif code[i] == "]":
            if arr[ptr] != 0:
                i = goto[i]

        i += 1

    return ret

def main():
    input = sys.stdin.readline
    T = int(input())
    for i in range(1, T+1):
        code = ""
        while (line := input().rstrip()) != "end":
            if (cut_idx := line.find("%")) != -1:
                code += line[:cut_idx]
            else: code += line
        print(f"PROGRAM #{i}:\n{compile_BF(code)}")


if __name__ == '__main__':
    main()