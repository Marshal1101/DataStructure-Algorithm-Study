import sys


def main():
    input = sys.stdin.readline
    D, N = map(int, input().split())
    oven = [*map(int, input().split())]
    ptr = D
    cnt = 0
    for r in map(int, input().split()):
        for i in range(ptr):
            if r > oven[i]:
                if i == 0:
                    print(ptr+1)
                    return
                ptr = i-1
                cnt += 1
                break
        else:
            ptr -= 1
    
    print(ptr+1)


if __name__ == '__main__':
    main()