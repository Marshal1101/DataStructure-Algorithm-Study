import sys 


input = sys.stdin.readline
str1 = input().rstrip()
str2 = input().rstrip()

dp = [[0 for _ in range(len(str1))] for _ in range(len(str2))]
maxleng = 0
for i in range(len(str2)):
    for j in range(len(str1)):
        if str2[i] == str1[j]:
            if i > 0 and j > 0 and dp[i-1][j-1] > 0:
                dp[i][j] += dp[i-1][j-1] + 1
                if dp[i][j] > maxleng: maxleng = dp[i][j]
            else:
                dp[i][j] = 1

for i in range(len(str2)):
    print(dp[i])

print(maxleng)