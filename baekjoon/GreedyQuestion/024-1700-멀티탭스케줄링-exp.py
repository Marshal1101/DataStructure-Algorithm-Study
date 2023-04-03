import sys
input = sys.stdin.readline

N,K = map(int,input().split())

seq = [*map(int,input().split())]

inuse = set()
cnt = 0
for i in range(K):
  if len(inuse) == N and seq[i] not in inuse:
    willuse = set()
    for j in range(i+1,K):
      if seq[j] in inuse:
        Pop = seq[j]
        willuse.add(seq[j])
        if len(willuse) == N:
          break
    if len(willuse) == N:
      inuse.remove(Pop)
    else:
      for Pop in inuse-willuse:
        inuse.remove(Pop)
        break
    cnt += 1
  inuse.add(seq[i])

print(cnt)