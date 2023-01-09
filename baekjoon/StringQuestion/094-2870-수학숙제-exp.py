import sys
input = sys.stdin.readline

n = int(input())
ans_list = []
for _ in range(n):
    word = input()
    i = 0
    temp = ''
    while i < len(word):
        if word[i].isdigit():
            temp += word[i]
        else:
            if temp:
                ans_list.append(int(temp))
                temp = ''
        i += 1
            
            
ans_list.sort()

for i in ans_list:
    print(i)