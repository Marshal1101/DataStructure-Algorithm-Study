from itertools import combinations as comb

e = input()
stack = []
pairs = []

for i in range(len(e)):
    if e[i] == "(":
        stack.append(i)

    elif e[i] == ")":
        pairs.append((stack.pop(), i))

result = set()
for r in range(1, len(pairs) + 1):
    for pair in comb(pairs, r):
        temp = list(e)
        for a, b in pair:
            temp[a] = temp[b] = ""
        result.add("".join(temp))

print(*sorted(result), sep="\n")
