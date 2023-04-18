from collections import deque

def main():
    S, P = map(int, input().split())
    ans = 0
    window = deque()
    arr = input().rstrip()
    acgt = dict()
    cnt = list(map(int, input().split()))
    acgt['A'] = cnt[0]
    acgt['C'] = cnt[1]
    acgt['G'] = cnt[2]
    acgt['T'] = cnt[3]
    window_cnt = {'A':0, 'C':0, 'G':0, 'T':0}
    for c in arr:
        window.append(c)
        window_cnt[c] += 1
        if len(window) < P:
            continue

        for key in window_cnt.keys():
            if window_cnt[key] < acgt[key]:
                break
        else:
            ans += 1
        
        pc = window.popleft()
        window_cnt[pc] -= 1

    print(ans)

if __name__ == '__main__':
    main()