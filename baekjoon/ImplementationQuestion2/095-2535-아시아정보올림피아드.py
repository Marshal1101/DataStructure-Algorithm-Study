import sys
# from heapq import heappop, heappush

def main():
    # input = sys.stdin.readline
    # N = int(input())
    # hq = []
    # for _ in range(N):
    #     nat, std, point = map(int, input().split())
    #     heappush(hq, (-point, nat, std))
    
    # winner = dict()
    # cnt = 0
    # while hq:
    #     point, nat, std = heappop(hq)
    #     if nat in winner:
    #         if winner[nat] == 2:
    #             continue
    #         winner[nat] += 1
    #     else:
    #         winner[nat] = 1
    #     print(nat, std)
    #     cnt += 1
    #     if cnt == 3:
    #         break
    
    input = sys.stdin.readline
    N = int(input())
    nom = [list(map(int, input().split())) for _ in range(N)]
    nom.sort(key=lambda x:x[2], reverse=True)
    cnt = 0
    winner = dict()
    for i in range(N):
        nat, std, point = nom[i]
        if nat in winner:
            if winner[nat] == 2:
                continue
            winner[nat] += 1
        else:
            winner[nat] = 1
        print(nat, std)
        cnt += 1
        if cnt == 3:
            break

if __name__ == '__main__':
    main()