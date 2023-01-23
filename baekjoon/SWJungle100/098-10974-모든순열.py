import sys

def permutation(k, N, used: list, ans: list):

    if k > N:
        print(" ".join(ans))
        return

    for i in range(1, N+1):
        if not used[i]:
            used[i] = True
            ans.append(str(i))
            permutation(k+1, N, used, ans)
            ans.pop()
            used[i] = False

N = int(sys.stdin.readline())
used = [False] * (N+1)
ans = []

permutation(1, N, used, ans)