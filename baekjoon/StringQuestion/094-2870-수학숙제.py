import sys


def parser(string: str) -> list:
    ans = []
    num = ""
    prev = ""
    is_begin_zero = False
    for c in string:
        if c == '0' and (prev < '0' or prev > '9'):
            is_begin_zero = True
        elif '0' <= c <= '9':
            num += c
            prev = c
        else:
            if num != "": ans.append(int(num))
            else:
                if is_begin_zero: ans.append(0)
            prev = c
            num = ""
            is_begin_zero = False
            
    if num: ans.append(int(num))
    else:
        if is_begin_zero: ans.append(0)

    return ans


def main():
    input = sys.stdin.readline
    N = int(input())
    ans_list = []
    for _ in range(N):
        ans_list += parser(input().rstrip())

    ans_list.sort()
    for n in ans_list:
        print(n)


if __name__ == '__main__':
    main()