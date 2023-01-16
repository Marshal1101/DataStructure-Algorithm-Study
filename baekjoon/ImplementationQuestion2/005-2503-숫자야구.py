import sys

from itertools import permutations

def main():
    input = sys.stdin.readline
    N = int(input())
    table = [input().split() for _ in range(N)]
    ans = set()
    num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for p1, p2, p3 in permutations(num_list, 3):
        num = p1 + p2 + p3
        flag = True
        for sbo, s, b in table:
            stk = 0
            bal = 0
            for i in range(3):
                if num[i] == sbo[i]:
                    stk += 1
                elif num[i] in sbo:
                    bal += 1
            if stk != int(s) or bal != int(b):
                flag = False
                break
        
        if flag: ans.add(num)

    print(len(ans))
    # print(ans)

if __name__ == '__main__':
    main()