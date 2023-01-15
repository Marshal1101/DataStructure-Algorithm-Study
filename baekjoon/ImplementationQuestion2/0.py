from collections import deque, defaultdict



tree = defaultdict(deque)

for i in range(1, 13):
    tree[i].append(i+i)


sorted_tree = sorted(tree.keys())
print(sorted_tree)


print(1//2)