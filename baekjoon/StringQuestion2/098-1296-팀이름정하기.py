import sys


def main():
    input = sys.stdin.readline
    
    name = input().rstrip()
    N = int(input())
    if N == 1:
        print(input().rstrip())
    love = {
        "L": 0,
        "O": 0,
        "V": 0,
        "E": 0
    }
    for c in name:
        if c in love:
            love[c] += 1
    arr = []
    for i in range(N):
        team = input().rstrip()
        copy_love = love.copy()
        for c in team:
            if c in copy_love:
                copy_love[c] += 1
        copy_list = list(copy_love.items())
        v = 1
        for i in range(len(copy_list)):
            for j in range(i+1, len(copy_list)):
                v *= copy_list[i][1] + copy_list[j][1]
        arr.append((v%100, team))
    
    arr.sort(key=lambda x: (-x[0], x[1]))
    print(arr[0][1])


if __name__ == '__main__':
    main()