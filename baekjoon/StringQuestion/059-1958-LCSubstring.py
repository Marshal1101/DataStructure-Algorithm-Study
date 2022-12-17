import sys; input = sys.stdin.readline


def LCS(s1: str, s2: str, s3: str) -> str:
    dp = [[["" for _ in range(len(s1))] for _ in range(len(s2))] for _ in range(len(s3))]
    maxleng = ""

    for i in range(len(s3)):
        for j in range(len(s2)):
            if s3[i] == s2[j]:
                for k in range(len(s1)):
                    if s2[j] == s1[k]:
                        if i > 0 and j > 0 and k > 0 and len(dp[i-1][j-1][k-1]) > 0:
                            dp[i][j][k] += dp[i-1][j-1][k-1] + s1[k]
                        else:
                            dp[i][j][k] = s1[k]
                        if len(dp[i][j][k]) > len(maxleng): maxleng = dp[i][j][k]

    return maxleng

s1 = input().rstrip()
s2 = input().rstrip()
s3 = input().rstrip()
print(len(LCS(s1, s2, s3)))
print(LCS(s1, s2, s3))