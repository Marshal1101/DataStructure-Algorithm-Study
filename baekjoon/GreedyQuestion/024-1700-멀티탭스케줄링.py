from collections import defaultdict

def main():
    ans = 0
    N, K = map(int, input().split())
    if N >= K:
        print(0)
        return
    arr = list(map(int, input().split()))
    stk = defaultdict(list)
    for i in range(K-1, -1, -1):
        stk[arr[i]].append(i)
    plug = set()
    for i in range(K):
        stk[arr[i]].pop()
        # 1. 플러그에 기기가 있으면 패스
        if arr[i] in plug:
            continue
        # 2. 플러그 비어있으면 기기 추가
        if len(plug) < N:
            plug.add(arr[i])
            continue
        # 3. 플러그 다 차서 하나 빼야할 때, 쓸일이 가장 뒤에 있는 기기 선택
        max_i = -1
        mp = -1
        for p in plug:
            if len(stk[p]) == 0:
                plug.remove(p)
                plug.add(arr[i])
                ans += 1
                break
            if stk[p][-1] > max_i:
                max_i = stk[p][-1]
                mp = p
        else:
            plug.remove(mp)
            plug.add(arr[i])
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()