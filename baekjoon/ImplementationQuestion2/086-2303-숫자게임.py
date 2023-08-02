import sys
from itertools import combinations

def main():
    input = sys.stdin.readline
    N = int(input())
    winner = 0
    winnum = 0
    for i in range(1, N+1):
        card = list(map(int, input().split()))
        for c in combinations(card, 3):
            num = sum(c) % 10
            if num >= winnum:
                winnum = num
                winner = i
                if num == 9:
                    break
    
    print(winner)


if __name__ == '__main__':
    main()



