import sys


def main() :
    input = sys.stdin.readline
    N = int(input())
    arr = list(input().split())
    M = int(input())

    dp = [[-1 for _ in range(N)] for _ in range(N)]
    for i in range(N) : 
        dp[i][i] = 1
        if arr[i] == arr[i+1] : dp[i][i+1] = 1
        else : dp[i][i+1] = 0
        

    for _ in range(M) :
        s_idx, e_idx = map(lambda x: int(x)-1, input().split())
        # ask.append(list(map(lambda x: int(x)-1, input().split())))

        if dp[s_idx][e_idx] == 1 :
            print('1')
        elif dp[s_idx][e_idx] == 0 :
            print('0')
        else :
            # idx 짝수 개일 때
            if (temp := e_idx + s_idx) % 2 :
                lp = temp // 2
                rp = lp + 1
            # idx 홀수 개일 때
            else :
                lp = rp = temp // 2

            while arr[lp] == arr[rp] :
                dp[lp][rp] = 1
                lp -= 1
                rp += 1
                if lp < s_idx and rp > e_idx :
                    print('1')
                    break
            else :
                dp[lp][rp] = 0
                print('0')


if __name__ == '__main__' :
    main()