import sys


def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        arr1 = input().rstrip()
        arr2 = input().rstrip()
        cnt = {"B": 0, "W": 0}
        for i in range(N):
            if arr1[i] != arr2[i]:
                cnt[arr1[i]] += 1
        
        ans = cnt["B"] if cnt["B"] > cnt["W"] else cnt["W"]
        print(ans)


if __name__ == '__main__':
    main()