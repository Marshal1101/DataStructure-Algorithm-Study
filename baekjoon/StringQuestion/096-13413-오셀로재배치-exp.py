# https://www.acmicpc.net/source/46385068

import sys

T = int(sys.stdin.readline())
for _ in range(T):
  n = int(sys.stdin.readline())
  str1 = sys.stdin.readline().strip()
  str2 = sys.stdin.readline().strip()

  diff = [a for a, b in zip(str1, str2) if a != b]
  w = diff.count('W')
  print(max(w, len(diff) - w))