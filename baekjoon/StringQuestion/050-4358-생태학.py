import sys
from collections import defaultdict

input = sys.stdin.readline
dicTree = defaultdict(int)
cnt = 0
while (treeName := input().rstrip()) != "":
    dicTree[treeName] += 1
    cnt += 1

sortedTree = list(dicTree.items())
sortedTree.sort()
for key, value in sortedTree:
    print(f"{key} {(value*100/cnt):.4f}")