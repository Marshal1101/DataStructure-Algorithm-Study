import sys; input = sys.stdin.readline
N = int(input())
point = dict()

words = []
for i in range(N):
    word = input().rstrip()
    for k in range(len(word)):
        if not word[k] in point:
            point[word[k]] = 10 ** (len(word)-1 - k)
        else:
            point[word[k]] += 10 ** (len(word)-1 - k)
    words.append(word)

num = 9
for alp, weight in sorted(point.items(), key=lambda x: -x[1]):
    point[alp] = str(num)
    num -= 1
total = 0
for word in words:
    tmp = ""
    for c in word:
        tmp += point[c]
    total += int(tmp)


print(total)