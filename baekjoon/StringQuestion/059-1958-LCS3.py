import sys; input = sys.stdin.readline


def LCS(s1: str, s2: str, s3: str) -> str:
    dp = [[[0 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)] for _ in range(len(s3)+1)]

    for i in range(len(s3)):
        for j in range(len(s2)):
            for k in range(len(s1)):
                if s3[i] == s2[j] == s1[k]:
                    dp[i+1][j+1][k+1] = dp[i][j][k] + 1
                else:
                    dp[i+1][j+1][k+1] = max(dp[i+1][j+1][k], dp[i+1][j][k+1], dp[i][j+1][k+1])
    
    # for i in range(len(s3)+1):
    #     print(f"======={i}========")
    #     for j in range(len(s2)+1):
    #         print(dp[i][j])

    return dp[len(s3)][len(s2)][len(s1)]

s1 = input().rstrip()
s2 = input().rstrip()
s3 = input().rstrip()
print(LCS(s1, s2, s3))