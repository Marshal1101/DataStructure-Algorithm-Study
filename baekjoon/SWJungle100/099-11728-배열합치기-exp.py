import sys
N,M = sys.stdin.readline().split()
print(' '.join(sorted(sys.stdin.read().split(), key=int)))