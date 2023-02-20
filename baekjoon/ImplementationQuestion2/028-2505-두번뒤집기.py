import sys




def main():
    input = sys.stdin.readline
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    copy = arr[:]
    ans = []
    idx = 1
    while idx != N:
        for i in range(idx, N+1):
            if idx == copy[idx]:
                break
            if copy[i] == idx:
                ans.append(f"{idx} {i}")
                copy[idx:i+1] = reversed(copy[idx:i+1])
        idx += 1

    if 0 < len(ans) <= 2:
        for _ in range(2-len(ans)):
            ans.append("1 1")
        print("\n".join(ans))
        return

    ans.clear()
    copy = arr[:]
    idx = N
    while idx != 1:
        for i in range(idx, 0, -1):
            if idx == copy[idx]:
                break
            if copy[i] == idx:
                ans.append(f"{i} {idx}")
                copy[i:idx+1] = reversed(copy[i:idx+1])
        idx -= 1

    if len(ans) <= 2:
        for _ in range(2-len(ans)):
            ans.append("1 1")
        print("\n".join(ans))


if __name__ == '__main__':
    main()