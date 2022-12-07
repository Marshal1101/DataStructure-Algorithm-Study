import sys


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arrDNA = [input().rstrip() for _ in range(N)]    
    
    retDNA = ""
    difCnt = 0
    for i in range(M):
        cnt = [0] * 4
        for j in range(N):
            if arrDNA[j][i] == "A": cnt[0] += 1
            elif arrDNA[j][i] == "C": cnt[1] += 1
            elif arrDNA[j][i] == "G": cnt[2] += 1
            elif arrDNA[j][i] == "T": cnt[3] += 1
        maxCnt = max(cnt)
        idx = cnt.index(maxCnt)
        if idx == 0: retDNA += "A" 
        elif idx == 1: retDNA += "C"
        elif idx == 2: retDNA += "G"
        elif idx == 3: retDNA += "T"
        difCnt += N - maxCnt

    print(retDNA)
    print(difCnt)


if __name__=='__main__':
    main()