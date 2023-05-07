import sys


def valid(a: int, b: int):
  return not (a == 1 and b == 3) and b != 4


def f(dp, n: int, p: int):
  if dp[n][p] != -1:
    return dp[n][p]

  ret = 0
  for i in range(10):
    if valid(p, i):
      ret += f(dp, n-1, i)
  dp[n][p] = ret
  return ret


def main():
  input = sys.stdin.readline
  dp = [[-1] * 10 for _ in range(13)]


  for i in range(10):
    dp[0][i] = 1

  T = int(input())
  for _ in range(T):
    ans = 0
    k, h = map(int, input().split())
    n = 1
    while k != 0:
      t = k % 10
      k //= 10
      for i in range(t):
        if valid(k%10, i):
          ans += f(dp, n-1, i)
      n += 1
    print(ans * h)


if __name__ == '__main__':
  main()