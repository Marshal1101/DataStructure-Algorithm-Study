import sys


def main():
  input = sys.stdin.readline
  T = int(input())
  for tcase in range(1, T+1):
    print(f"Case #{tcase}:")
    a, b, x, m, n = map(int, input().split())

    f = [[0] * 6 for _ in range(120000)]
    calc = [[0] * 11000 for _ in range(6)] 
    deleted = [False] * 120000

    a %= m; b %= m; x %= m;

    for r in range(1, n+1):
      for c in range(1, 6):
          f[r][c] = (a * f[r-1][c] + b * f[r][c-1] + x) % m
          calc[c][f[r][c]] += 1

    q = int(input())

    while q > 0:
      q -= 1
      line = input().split()
      
      if line[0] == "insert":
        n += 1
        for i in range(1, 6):
          f[n][i] = int(line[i])
          calc[i][f[n][i]] += 1
      
      elif line[0] == "remove":
        r = int(line[1])
        if r <= n and not deleted[r]:
          deleted[r] = True
          for i in range(1, 6):
            calc[i][f[r][i]] -= 1
      
      elif line[0] == "max":
        c = int(line[1])
        for i in range(10000, -1, -1):
          if calc[c][i] != 0:
            print(i)
            break
      
      elif line[0] == "min":
        c = int(line[1])
        for i in range(10001):
          if calc[c][i] != 0:
            print(i)
            break

      elif line[0] == "range":
        c, left, right = map(int, line[1:])
        sum = 0
        for i in range(left, right+1):
          sum += calc[c][i]
        print(sum)


if __name__ == '__main__':
  main()