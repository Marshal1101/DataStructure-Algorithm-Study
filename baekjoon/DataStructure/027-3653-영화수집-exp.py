import sys
input = sys.stdin.readline

def update(i,v):
  while i<K:
    fen[i] += v
    i += i&-i

def SUM(i):
  s = 0
  while i:
    s += fen[i]
    i -= i&-i
  return s

for _ in range(int(input())):
  N,M = map(int,input().split()); K = 1<<18
  movie = [*map(int,input().split())]
  
  Index = [i+(1<<17) for i in range(N+1)]; top = 1<<17
  fen = [0]*K
  
  for n in range(1,N+1):
    update(Index[n],1)
  
  result = []
  for n in movie:
    result.append(SUM(Index[n]-1))
    update(Index[n],-1)
    Index[n] = top; update(top,1); top -= 1
  print(*result)