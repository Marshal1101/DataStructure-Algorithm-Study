import sys; input = sys.stdin.readline


def search(src: str, target: str) -> int:
    cnt = 0
    begin = 0
    while begin + len(target) <= len(src):
        matched = True
        for i in range(len(target)):
            if src[begin + i] != target[i]:
                matched = False
                break
        if matched:
            begin += len(target)
            cnt += 1
        else: begin += 1
    
    return cnt


def main():
    src = input().rstrip()
    target = input().rstrip()
    print(search(src, target))


if __name__ == '__main__':
    main()