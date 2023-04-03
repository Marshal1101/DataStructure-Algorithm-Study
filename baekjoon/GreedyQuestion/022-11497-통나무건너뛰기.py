import sys

def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        max_h = 0
        desc = sorted(map(int, input().split()), reverse=True)
        left = desc[0]
        right = desc[0]
        is_right = True
        for i in range(1, N):
            if is_right:
                h = right - desc[i]
                if h > max_h:
                    max_h = h
                right = desc[i]
                is_right = False
            else:
                h = left - desc[i]
                if h > max_h:
                    max_h = h
                left = desc[i]
                is_right = True
        print(max_h)

if __name__ == '__main__':
    main()